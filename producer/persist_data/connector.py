"""Configures a Kafka Connector for a postgresql database"""

import json
import requests
import time


def create_connector(name, url, kafka_connect_url, table_name, topic_name):
    # Define the connector configuration
    connector_config = {
        "name": name,
        "config": {
            "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
            "tasks.max": "1",
            "connection.url": "jdbc:postgresql://" + url,
            "connection.user": "myuser",
            "connection.password": "mypassword",
            "topics": topic_name,
            "table.name.format": table_name,
            "auto.create": "true",
            "insert.mode": "upsert",
            "pk.mode": "record_value",
            "pk.fields": "timestamp",
            "key.converter": "io.confluent.connect.avro.AvroConverter",
            "key.converter.schema.registry.url": "http://schema-registry:8081",
            "value.converter": "io.confluent.connect.avro.AvroConverter",
            "value.converter.schema.registry.url": "http://schema-registry:8081",
            "schema.registry.url": "http://schema-registry:8081"
        }
    }

    # Encode the connector configuration as JSON
    config_json = json.dumps(connector_config)

    # Create the connector using the Kafka Connect REST API
    response = requests.post(
        url=kafka_connect_url,
        headers={"Content-Type": "application/json"},
        data=config_json
    )

    # Check the response status code
    if response.status_code == 201:
        print("Connector created successfully with topic: " + topic_name)
    else:
        print("Error creating connector: {}".format(response.text))


# Create the connector
if __name__ == "__main__":
    time.sleep(15) # Wait that the sink connector is up and running

    create_connector(
        name="postgres-connector-traffic",
        url="postgres:5432/mydatabase",
        kafka_connect_url="http://connect:8083/connectors",
        table_name="raw_traffic",
        topic_name="raw_trafficdata"
    )
    create_connector(
        name="postgres-connector-weather",
        url="postgres:5432/mydatabase",
        kafka_connect_url="http://connect:8083/connectors",
        table_name="raw_weather",
        topic_name="raw_weatherdata"
    )
