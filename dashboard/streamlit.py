import streamlit as st
from kafka import KafkaConsumer
import json
import pandas as pd
import time

print("Starting consumer. Waiting for kafka to start up")
time.sleep(20)

# Define kafka consumer
consumer = KafkaConsumer("processed_trafficdata",
                         bootstrap_servers=['kafka1:9092', 'kafka2:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True)

st.title('Weather data sensor count')
st.markdown('This is a live stream of the sensor count')

# Initialize empty dataframe
df = pd.DataFrame(columns=['sensor_id', 'count'])
barchart = st.empty()

# DATA STREAM AND VISUALIZATION
while True:
    data = consumer.poll(timeout_ms=200)

    if not data:
        continue

    for key, value in data.items():

        for record in value:
            value_count = json.loads(record.value)
            sensor_id = json.loads(record.key)

            # Check if sensor id already exists in dataframe
            if sensor_id in df['sensor_id'].values:
                df.loc[df['sensor_id'] == sensor_id, 'count'] = value_count
            else:
                # Add new data to dataframe
                df = pd.concat([df, pd.DataFrame({'sensor_id': [sensor_id], 'count': [value_count]})],
                               ignore_index=True)

    # Update streamlit bar chart
    with barchart:
        st.bar_chart(df, x='sensor_id', y='count')

# Start Streamlit app
# streamlit run dashboard/streamlit.py