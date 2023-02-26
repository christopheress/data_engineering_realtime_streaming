#!/bin/bash

# Wait for Kafka and Schema Registry to start
while ! nc -z kafka1 9092; do
  echo "Waiting for Kafka to start..."
  sleep 1
done

while ! nc -z schema-registry 8081; do
  echo "Waiting for Schema Registry to start..."
  sleep 1
done

while ! nc -z connect 8083; do
  echo "Waiting for Kafka Connect to start..."
  sleep 1
done

echo "Kafka, Connect and Schema Registry are running. Starting services ..."
