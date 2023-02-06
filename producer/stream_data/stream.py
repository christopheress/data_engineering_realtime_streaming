import faust
import models

# 1. Define the application
app = faust.App('sensor_counts',
                broker=['kafka://kafka1:9092', 'kafka://kafka2:9092'],
                # ['kafka://kafka1:9092', 'kafka://kafka2:9092'], #['kafka://localhost:8097', 'kafka://localhost:8098']
                web_port=6666)

# 2. Input stream
traffic_count_topic = app.topic('raw_trafficdata', value_type=models.TrafficModel)
processed_data_topic = app.topic('processed_trafficdata')

# 3. Define faust table
sensor_counts = app.Table('data_counts', default=int, partitions=2)


# 4. Define agent
@app.agent(traffic_count_topic)
async def count_data(stream):
    async for payload in stream:
        sensor_id = payload.sensor_id
        sensor_counts[sensor_id] += 1


# Send data to output stream every second
@app.timer(interval=2.0)
async def send_data():
    for sensor_id, count in sensor_counts.items():
        await processed_data_topic.send(key=sensor_id, value=count)
        print(f"Sent {count} for sensor {sensor_id}")


def main() -> None:
    app.main()

# 5. Run the agent in terminal
# faust -A stream worker -l info
