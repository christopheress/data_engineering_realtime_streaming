from database.database_functions import Database
from kafka import KafkaConsumer

import json
import requests

def create_connector():

    # Define the connector configuration
    connector_config = {
        "name": "my-sink-connector",
        "config": {
            "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
            "tasks.max": "1",
            "connection.url": "jdbc:postgresql://localhost:5432/mydatabase",
            "connection.user": "myuser",
            "connection.password": "mypassword",
            "topics": "raw_trafficdata",
            "table.name.format": "my_table",
            "auto.create": "true",
            "insert.mode": "upsert",
            "pk.mode": "record_value",
            "pk.fields": "id",
            "table.name.format": "my_table"
        }
    }

    # Encode the connector configuration as JSON
    config_json = json.dumps(connector_config)

    # Create the connector using the Kafka Connect REST API
    response = requests.post(
        "http://localhost:8083/connectors",
        headers={"Content-Type": "application/json"},
        data=config_json
    )

    # Check the response status code
    if response.status_code == 201:
        print("Connector created successfully")
    else:
        print("Error creating connector: {}".format(response.text))

# Create the connector
#resp = requests.get("http://localhost:8083/connectors/my-sink-connector")
#print(resp.content)
create_connector()

