import pika
import json
import time

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='payment_queue')

for i in range(200):
    message = {
        "type": "payment",
        "payment_id": i + 101,
        "user_email": f"user_payment{i + 1}@example.com",
        "amount": 49.99 + i
    }
    channel.basic_publish(
        exchange='',
        routing_key='payment_queue',
        body=json.dumps(message)
    )
    print(f"[payment] Sent payment #{message['payment_id']} of ${message['amount']}")
    time.sleep(1.5)

connection.close()
