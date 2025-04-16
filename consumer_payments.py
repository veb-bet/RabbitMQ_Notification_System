import pika
import json

def callback(ch, method, properties, body):
    message = json.loads(body)
    if message['type'] == 'payment':
        print(f"💰 Payment: #{message['payment_id']} of ${message['amount']} from {message['user_email']}")

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='payment_queue')

channel.basic_consume(queue='payment_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for payments. To exit press CTRL+C')
channel.start_consuming()
