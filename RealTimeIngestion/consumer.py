from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'shopping_cart_events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='shopping_cart_group',
    value_deserializer=lambda x: x.decode('utf-8')
    )

print("Kafka Consumer has been initiated...")

for message in consumer:
    print(f"Received: {message.value}")