# Streamlit application for the dashboard

import streamlit as st
from kafka import KafkaConsumer
import json
import pandas as pd
import time

print("Starting consumer. Waiting for kafka to start up")
time.sleep(20)

# Define kafka consumer
consumer_traffic = KafkaConsumer("processed_trafficdata",
                                 bootstrap_servers=['kafka1:9092', 'kafka2:9092'],
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=True)

consumer_weather = KafkaConsumer("processed_weatherdata",
                                 bootstrap_servers=['kafka1:9092', 'kafka2:9092'],
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=True)

st.title('Traffic data sensor count')
st.markdown('This is a live stream of the sensor count')

# Initialize empty dataframe
df_traffic = pd.DataFrame(columns=['sensor_id', 'count'])
barchart_traffic = st.empty()

# Elements for weather data
st.title('Weather data temperature distribution')
st.markdown('This is a live stream of the temperature distribution')

df_weather = pd.DataFrame(columns=['temperature', 'count'])
barchart_weather = st.empty()

# DATA STREAM AND VISUALIZATION
while True:
    data_traffic = consumer_traffic.poll(timeout_ms=2000)

    if not data_traffic:
        continue

    for key, value in data_traffic.items():

        for record in value:
            value_count = json.loads(record.value)
            sensor_id = json.loads(record.key)

            # Check if sensor id already exists in dataframe
            if sensor_id in df_traffic['sensor_id'].values:
                df_traffic.loc[df_traffic['sensor_id'] == sensor_id, 'count'] = value_count
            else:
                # Add new data to dataframe
                df_traffic = pd.concat([df_traffic, pd.DataFrame({'sensor_id': [sensor_id], 'count': [value_count]})],
                                       ignore_index=True)

    # Update streamlit bar chart
    with barchart_traffic:
        st.bar_chart(df_traffic, x='sensor_id', y='count')

    # Second consumer
    data_weather = consumer_weather.poll(timeout_ms=2000)

    if not data_weather:
        continue

    for key, value in data_weather.items():

        for record in value:
            value_count = json.loads(record.value)
            temperature = json.loads(record.key)

            # Check if temperature already exists in dataframe
            if temperature in df_weather['temperature'].values:
                df_weather.loc[df_weather['temperature'] == temperature, 'count'] = value_count
            else:
                # Add new data to dataframe
                df_weather = pd.concat(
                    [df_weather, pd.DataFrame({'temperature': [temperature], 'count': [value_count]})],
                    ignore_index=True)

    # Update streamlit bar chart
    with barchart_weather:
        st.bar_chart(df_weather, x='temperature', y='count')

# Start Streamlit app
# streamlit run dashboard/streamlit.py
