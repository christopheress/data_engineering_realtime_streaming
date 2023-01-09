import streamlit as st

consumer = st.kafka_consumer(consumer)

# Display the data in a chart
chart = st.line_chart(consumer.data)

# Or display the data in a table
table = st.table(consumer.data)

