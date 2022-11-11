import json
from kafka import KafkaConsumer
# Kafka Consumer
consumer = KafkaConsumer(
    'RawSensorData',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest'
)
for message in consumer:
    print(message.value)