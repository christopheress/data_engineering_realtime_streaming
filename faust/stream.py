import json
import faust
import pandas as pd


class Sensordata(faust.Record, serializer='json'):
    battery_life: float
    beach: str
    measurement_id: int
    sensor_id: int
    timestamp: str
    turbidity: float
    water_temperature: float


app = faust.App('sensor_app',  broker=['kafka://localhost:8097', 'kafka://localhost:8098'])
sensor_topic = app.topic('raw_sensor_data', partitions=2)


#requests_count_table = app.Table('requests_count', default=int, partitions=2)


@app.agent(sensor_topic)
async def myagent(stream):
    async for payload in stream:
        data = pd.DataFrame([payload])
        #requests_count_table[event.sensor_id] += 1
        print(data)


if __name__ == '__main__':
    app.main()

# docker exec -it bea900a8ef9e2a89ae75f1d4a7f9857b267311b19c1f151c38ab88a278ed4bb2 sh
# cd /opt/kafka_2.13-2.8.1/bin
# kafka-console-consumer.sh --topic RawSensorData --from-beginning --bootstrap-server localhost:9092
# bin/kafka-topics.sh --list --zookeeper localhost:2181
