import faust
import os

# 1. Define the application
app = faust.App('sensor_counts',
                broker=['kafka://localhost:8097', 'kafka://localhost:8098'],
                topic_partitions=os.getenv('KAFKA_NUM_PARTITIONS', 2),
                web_port=6666)


# 2. Model definition
class SensorCount(faust.Record):
    sensor_id: int
    timestamp: str
    temperature: float
    air_humidity: float
    wind_speed: float
    sunshine: bool


class TrafficData(faust.Record):
    timestamp: str
    long: int
    lat: float
    cars_ratio: float


# 3. Input stream
traffic_count_topic = app.topic('raw_trafficdata', value_type=TrafficData,
                                partitions=os.getenv('KAFKA_NUM_PARTITIONS', 2))

# 4. Define faust table
sensor_counts = app.Table('data_count', default=int, partitions=os.getenv('KAFKA_NUM_PARTITIONS', 2))


# 5. Define agent
@app.agent(traffic_count_topic)
async def count_data(stream):
    async for payload in stream:  # .group_by(SensorCount.sensor_id)
        sensor_counts[payload.sensor_id] += 1


if __name__ == '__main__':
    app.main()

# faust -A stream worker -l info
# docker exec -it 67974ec0928ed396337faff5f2e25aa3c814e0291d39820ca81047b6e584b2d9 bash
# kafka-console-producer --broker-list localhost:8097 localhost:8098 --topic raw_sensor_data
# kafka-console-consumer --bootstrap-server kafka1:9092 --topic raw_sensor_data --from-beginning
# cd /opt/kafka_2.13-2.8.1/bin
# kafka-console-consumer.sh --topic RawSensorData --from-beginning --bootstrap-server localhost:9092
# bin/kafka-topics.sh --list --zookeeper localhost:2181

# $KAFKA_HOME/bin/kafka-console-consumer --topic sensor_counts-sensor_counts-changelog --bootstrap-server localhost:8098 --property print.key=True --from-beginning
