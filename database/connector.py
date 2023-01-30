"""Configures a Kafka Connector for a postgresql database"""

import json
import requests


def create_connector(name, url, kafka_connect_url):
    # Define the connector configuration
    connector_config = {
        "name": name,
        "config": {
            "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
            "tasks.max": "1",
            "connection.url": "jdbc:postgresql://" + url,
            "connection.user": "myuser",
            "connection.password": "mypassword",
            "topics": "raw_trafficdata",
            "table.name.format": "my_table",
            "auto.create": "true",
            "insert.mode": "upsert",
            "pk.mode": "record_value",
            "pk.fields": "id"
            # key.converter
            # value.converter
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
        print("Connector created successfully")
    else:
        print("Error creating connector: {}".format(response.text))


# Create the connector
create_connector(name='postgresql_connector',
                 url='localhost:5432/mydatabase',
                 kafka_connect_url='http://localhost:8083/connectors')
