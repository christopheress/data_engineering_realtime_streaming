from schema_registry.client import SchemaRegistryClient, schema
from schema_registry.serializers import AvroMessageSerializer
from schema_registry.serializers.faust import FaustSerializer

weather_schema = {
    "namespace": "weather.value",
    "type": "record",
    "name": "weather.value",
    "fields": [
        {
            "name": "sensor_id",
            "type": "string"
        },
        {
            "name": "temperature",
            "type": "double"
        },
        {
            "name": "air_humidity",
            "type": "double"
        },
        {
            "name": "wind_speed",
            "type": "double"
        },
        {
            "name": "sunshine",
            "type": "boolean"
        }
    ]
}

traffic_schema = {
    "type": "record",
    "name": "traffic.value",
    "namespace": "traffic.value",
    "fields": [
        {
            "name": "sensor_id",
            "type": "string"
        },
        {
            "name": "long",
            "type": "string"
        },
        {
            "name": "lat",
            "type": "string"
        },
        {
            "name": "cars_ratio",
            "type": "double"
        }
    ]
}

client = SchemaRegistryClient(url="http://0.0.0.0:8081/")

avro_weather_serializer = AvroMessageSerializer(client, "weather", schema.AvroSchema(weather_schema))
avro_traffic_serializer = AvroMessageSerializer(client, "traffic", schema.AvroSchema(traffic_schema))
avro_traffic_serializer = FaustSerializer(client, "traffic", traffic_schema)
avro_weather_serializer = FaustSerializer(client, "weather", weather_schema)


# function used to register the codec
def avro_traffic_codec():
    return avro_traffic_serializer


def avro_weather_codec():
    return avro_weather_serializer


# Send the schema to the registry
def init_schema(url_registry="http://schema-registry:8081/"):
    client = SchemaRegistryClient(url=url_registry)
    client.register('weatherdata', schema.AvroSchema(weather_schema))
    client.register('trafficdata', schema.AvroSchema(traffic_schema))
