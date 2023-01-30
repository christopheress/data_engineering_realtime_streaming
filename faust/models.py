import faust
from dataclasses_avroschema import AvroModel

class WeatherModel(faust.Record, AvroModel, serializer='avro_weather'):
    sensor_id: str
    temperature: float
    air_humidity: float
    wind_speed: float
    sunshine: bool

class TrafficModel(faust.Record, AvroModel, serializer='avro_traffic'):
    sensor_id: str
    long: str
    lat: str
    cars_ratio: float