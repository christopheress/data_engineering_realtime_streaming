# Streamlit application for the dashboard

import json

import pandas as pd
from kafka import KafkaConsumer

import streamlit as st

brokers = ['localhost:8097', 'localhost:8098']#['kafka1:9092', 'kafka2:9092'] # ['localhost:8097', 'localhost:8098'] for local testing


class DataStream:
    def __init__(self, topic, columns):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=brokers,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
        )
        self.df = pd.DataFrame(columns=columns)
        self.barchart = st.empty()

    def update_data_df(self, column):

        """
        This function updates the dataframe with new data received from the Kafka consumer.
        """

        data = self.consumer.poll(timeout_ms=2000)

        if not data:
            return

        for key, value in data.items():
            for record in value:
                value_count = json.loads(record.value)
                key_value = json.loads(record.key)

                # If the key value is already in the dataframe, update the count value
                if key_value in self.df[column].values:
                    self.df.loc[self.df[column] == key_value, "count"] = value_count

                # If the key value is not in the dataframe, add a new row to the dataframe
                else:
                    self.df = pd.concat([self.df,
                                         pd.DataFrame({
                                             column: [key_value],
                                             "count": [value_count]})],
                                        ignore_index=True)


class TrafficData(DataStream):
    """
    This class is used to update the traffic data chart.
    """
    def __init__(self):
        super().__init__("processed_trafficdata", ["sensor_id", "count"])

    def update_chart(self):
        with self.barchart:
            st.bar_chart(self.df, x="sensor_id", y="count")


class WeatherData(DataStream):
    """
    This class is used to update the weather data chart.
    """
    def __init__(self):
        super().__init__("processed_weatherdata", ["temperature", "count"])

    def update_chart(self):
        with self.barchart:
            st.bar_chart(self.df, x="temperature", y="count")


def main():
    st.title("Traffic data sensor count")
    st.markdown("This is a live stream of the sensor count")
    traffic_data = TrafficData()

    st.title("Weather data temperature distribution")
    st.markdown("This is a live stream of the temperature distribution")
    weather_data = WeatherData()

    while True:
        traffic_data.update_data_df(column="sensor_id")
        traffic_data.update_chart()

        weather_data.update_data_df(column="temperature")
        weather_data.update_chart()


if __name__ == "__main__":
    main()

# Start Streamlit app
# streamlit run dashboard/streamlit.py
