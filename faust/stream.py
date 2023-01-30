import faust
import os
import models


# 1. Define the application
app = faust.App('sensor_counts',
                broker=['kafka://localhost:8097', 'kafka://localhost:8098'],
                #topic_partitions=os.getenv('KAFKA_NUM_PARTITIONS', 2),
                #partitions=os.getenv('KAFKA_NUM_PARTITIONS', 2),
                web_port=6666)


# 2. Input stream
traffic_count_topic = app.topic('raw_trafficdata', value_type=models.TrafficModel) #, partitions=os.getenv('KAFKA_NUM_PARTITIONS', 2)
processed_data_topic = app.topic('processed_trafficdata')

# 3. Define faust table
sensor_counts = app.Table('data_counts', default=int, partitions=os.getenv('KAFKA_NUM_PARTITIONS', 2))




# 4. Define agent
@app.agent(traffic_count_topic)
async def count_data(stream):
    async for payload in stream:  # .group_by(SensorCount.sensor_id)
        sensor_id = payload.sensor_id
        sensor_counts[sensor_id] += 1

        if(sensor_counts[sensor_id] % 20 == 0):
            print(f"Sensor {sensor_id} has {sensor_counts[sensor_id]} counts")
            await processed_data_topic.send(
                key=sensor_id,
                value=sensor_counts[sensor_id]
            )

#@app.agent(traffic_count_topic)
#async def count_hits(counts):
 #   async for count in counts:
 #       print(f"Data recieved is {count}")
 #       if sensor_counts[sensor_id] > 20:
 #           await sensor_counts.send(value=count)


#@app.agent(processed_data_topic)
#async def increment_count(counts):
#    async for count in counts:
#        print(f"Count in internal topic is {count}")
 #        sensor_counts[str(count.sensor_id)]+=1
 #       print(f'{str(count.sensor_id)} has now been seen {sensor_counts[str(count.sensor_id)]} times')


def main() -> None:
    app.main()


# faust -A stream worker -l info
# docker exec -it 67974ec0928ed396337faff5f2e25aa3c814e0291d39820ca81047b6e584b2d9 bash
# kafka-console-producer --broker-list localhost:8097 localhost:8098 --topic raw_sensor_data
# kafka-console-consumer --bootstrap-server kafka1:9092 --topic raw_sensor_data --from-beginning
# cd /opt/kafka_2.13-2.8.1/bin
# kafka-console-consumer.sh --topic RawSensorData --from-beginning --bootstrap-server localhost:9092
# bin/kafka-topics.sh --list --zookeeper localhost:2181

# $KAFKA_HOME/bin/kafka-console-consumer --topic sensor_counts-sensor_counts-changelog --bootstrap-server localhost:8098 --property print.key=True --from-beginning
