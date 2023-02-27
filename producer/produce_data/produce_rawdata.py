import time
from os import environ

import requests
from kafka import KafkaProducer
from schema_registry.client import SchemaRegistryClient
from schema_registry.serializers import AvroMessageSerializer

import schema


class DataStreamer:
    def __init__(self):
        if environ.get('DOCKER') is not None:
            self.server = ['kafka1:9092', 'kafka2:9092']
            self.flask_link = 'flask'
            self.link_schema = "http://schema-registry:8081/"
            print('Stage: Docker')
        else:
            self.server = ['localhost:8097', 'localhost:8098']
            self.flask_link = '0.0.0.0'
            self.link_schema = "http://127.0.0.1:8081"
            print('Stage: Local')

        self.client = SchemaRegistryClient(self.link_schema)
        self.avro_message_serializer = AvroMessageSerializer(self.client)

    def get_data_stream(self, source='trafficdata'):
        """
            Retrieves data from a Flask API and encodes it in Avro format.

            Args:
                source (str): The data source to retrieve from the API (default is 'trafficdata').

            Returns:
                bytes: The encoded data in Avro format.

                If there was an error retrieving the data, returns the string "Error in Connection".
        """
        try:
            url = 'http://' + self.flask_link + ':3030/' + source + '/'
            answer = requests.get(url)

            # Get the schema ID for the specified topic and version from the Schema Registry client.
            id_schema = self.client.get_schema('raw_' + source + '-value', 1).schema_id
            avro_answer = self.avro_message_serializer.encode_record_with_schema_id(id_schema, answer.json())
            return avro_answer
        except:
            return "Error in Connection"

    def start(self):
        """
            Starts the Kafka producer and continuously sends data to Kafka topics.

            Initializes the schema Avro registry and creates a Kafka producer object.
            Retrieves data from two Flask API endpoints using the get_data_stream method and sends the encoded data
            to two Kafka topics ('raw_trafficdata' and 'raw_weatherdata') using the producer object.

        """
        schema.init_schema(url_registry=self.link_schema)  # Initialize the schema Avro registry
        producer = KafkaProducer(bootstrap_servers=self.server)  # Create a Kafka producer object

        while True:
            msg_traffic = self.get_data_stream(source='trafficdata')
            producer.send(topic="raw_trafficdata", value=msg_traffic)

            msg_weather = self.get_data_stream(source='weatherdata')
            producer.send(topic="raw_weatherdata", value=msg_weather)
            # time.sleep(0.1)


if __name__ == '__main__':
    time.sleep(10)  # Wait that kafka topics are created
    streamer = DataStreamer()
    streamer.start()
