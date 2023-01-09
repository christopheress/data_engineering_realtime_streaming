import time
from os import environ
import requests
from kafka import KafkaProducer


# Variables depend on environment
if environ.get('DOCKER') is not None:
    server = ['kafka1:9092', 'kafka2:9092']
    flask_link = 'flask'
    print('Stage: Docker')
else:
    server = ['localhost:8097', 'localhost:8098']
    flask_link = '0.0.0.0'
    print('Stage: Local')


def get_data_stream(source='trafficdata'):
    try:
        url = 'http://' + flask_link + ':3030/' + source + '/'
        r = requests.get(url)
        return r.text
    except:
        return "Error in Connection"


if __name__ == '__main__':

    time.sleep(20)  # Wait for Kafka Brokers

    producer = KafkaProducer(
        bootstrap_servers=server
    )
    while True:
        msg_traffic = get_data_stream(source='trafficdata')
        producer.send(topic="raw_trafficdata", value=msg_traffic.encode('utf-8'))

        msg_weather = get_data_stream(source='weatherdata')
        producer.send(topic="raw_weatherdata", value=msg_traffic.encode('utf-8'))
        time.sleep(1)
