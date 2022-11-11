import json
from sseclient import SSEClient as EventSource
from kafka import KafkaProducer

# Create producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'] #Kafka server
)

# Read streaming event
url = 'https://stream.wikimedia.org/v2/stream/recentchange'
try:
    for event in EventSource(url):
        if event.event == 'message':
            try:
                change = json.loads(event.data)
            except ValueError:
                pass
            else:
                #Send msg to topic wiki-changes
                producer.send('wiki-changes', change)

except KeyboardInterrupt:
    print("process interrupted")


