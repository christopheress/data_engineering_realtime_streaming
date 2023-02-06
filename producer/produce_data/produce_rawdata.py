import time
from os import environ
import requests
from kafka import KafkaProducer
from schema_registry.client import SchemaRegistryClient
from schema_registry.serializers import AvroMessageSerializer
import schema

# Variables depend on environment
if environ.get('DOCKER') is not None:
    server = ['kafka1:9092', 'kafka2:9092']
    flask_link = 'flask'
    link_schema = "http://schema-registry:8081/"
    print('Stage: Docker')
else:
    server = ['localhost:8097', 'localhost:8098']
    flask_link = '0.0.0.0'
    link_schema = "http://127.0.0.1:8081"
    print('Stage: Local')


client = SchemaRegistryClient(link_schema)
avro_message_serializer = AvroMessageSerializer(client)

def get_data_stream(source='trafficdata'):
    try:
        url = 'http://' + flask_link + ':3030/' + source + '/'
        answer = requests.get(url)

        id_schema = client.get_schema(source, 1).schema_id
        avro_answer = avro_message_serializer.encode_record_with_schema_id(id_schema, answer.json())
        return avro_answer
    except:
        return "Error in Connection"


if __name__ == '__main__':

    time.sleep(15)
    schema.init_schema(url_registry=link_schema)  # Create schema avro registry
    producer = KafkaProducer(bootstrap_servers=server)

    while True:
        msg_traffic = get_data_stream(source='trafficdata')
        producer.send(topic="raw_trafficdata", value=msg_traffic)

        msg_weather = get_data_stream(source='weatherdata')
        producer.send(topic="raw_weatherdata", value=msg_weather)
        #time.sleep(0.1)
