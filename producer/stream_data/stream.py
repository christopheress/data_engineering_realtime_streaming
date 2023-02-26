import time
import faust
from models import TrafficModel, WeatherModel

# 0. Wait that kafka topics are created
time.sleep(5)

# 1. Define the application
app = faust.App('sensor_counts',
                broker=['kafka://kafka1:9092', 'kafka://kafka2:9092'],
                web_port=6666)

# 2. Input stream
traffic_count_topic = app.topic('raw_trafficdata', value_type=TrafficModel)
weather_temperature_topic = app.topic('raw_weatherdata', value_type=WeatherModel)

# 2.1 Output stream
processed_data_traffic = app.topic('processed_trafficdata')
processed_data_weather = app.topic('processed_weatherdata')

# 3. Define faust table
sensor_counts = app.Table('data_counts', default=int, partitions=2)
temperature_histogram = app.Table('temperature_histogram', default=int, partitions=2)


# 4. Define agents
@app.agent(traffic_count_topic)
async def count_data(stream: faust.Stream[TrafficModel]) -> None:
    async for payload in stream:
        sensor_id = payload.sensor_id
        sensor_counts[sensor_id] += 1

@app.agent(weather_temperature_topic)
async def create_histogram_data(stream: faust.Stream[WeatherModel]) -> None:
    async for payload in stream:
        temperature = round(payload.temperature)
        temp_index = str(temperature)
        temperature_histogram[temp_index] += 1

# 5. Define timer function to send data to output streams
@app.timer(interval=2.0)
async def send_processed_data() -> None:
    for sensor_id, count in sensor_counts.items():
        await processed_data_traffic.send(key=sensor_id, value=count)

    for temperature, count in temperature_histogram.items():
        await processed_data_weather.send(key=str(temperature), value=count)



# 6. Run the agent in terminal
# faust -A stream worker -l info
if __name__ == '__main__':
    app.main()
