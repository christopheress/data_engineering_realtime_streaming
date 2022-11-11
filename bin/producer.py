import time
import requests
from kafka import KafkaProducer


def get_sensor_data_stream(max_sensors, number_sensors):
    try:
        url = 'http://0.0.0.0:3030/sensordata/' + str(max_sensors) + '/' + str(number_sensors)
        r = requests.get(url)
        return r.text
    except:
        return "Error in Connection"


# Create producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:8097', 'localhost:8098']  # Kafka server
)

while True:
    msg = get_sensor_data_stream(number_sensors=1, max_sensors=2)
    producer.send(topic="raw_sensor_data", value=msg.encode('utf-8'))
    time.sleep(0.1)
