from kafka import KafkaProducer
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: str(v).encode('utf-8')
    )

topic_name = 'shopping_cart_events'
print("Kafka Producer has been initiated...")

for i in range(1,10):
    message = f"Event {i}: User added item to shopping cart"
    producer.send(topic_name, value=message)
    print(f"Sent: {message}")
    time.sleep(1)

producer.flush()
print("All messages have been sent.")
producer.close()
