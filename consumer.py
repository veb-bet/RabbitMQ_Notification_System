import pika
import json

def callback(ch, method, properties, body):
    message = json.loads(body)
    if message['type'] == 'new_order':
        print(f"New order: #{message['order_id']} for {message['user_email']}")
    elif message['type'] == 'payment':
        print(f"Payment: #{message['payment_id']} of ${message['amount']} from {message['user_email']}")
    else:
        print("Unknown message type")

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='notification_queue')

channel.basic_consume(queue='notification_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for all types of notifications. To exit press CTRL+C')
channel.start_consuming()
