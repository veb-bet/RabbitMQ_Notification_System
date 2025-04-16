import pika
import json
import time

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='notification_queue')

for i in range(300):
    message = {
        "type": "new_order",
        "order_id": i + 1,
        "user_email": f"user{i + 1}@example.com"
    }
    channel.basic_publish(
        exchange='',
        routing_key='notification_queue',
        body=json.dumps(message)
    )
    print(f"[order] Sent order #{message['order_id']}")
    time.sleep(1)

connection.close()
