CREATE TABLE IF NOT EXISTS raw_weather (
    timestamp timestamp,
    sensor_id TEXT,
    temperature NUMERIC,
    air_humidity NUMERIC,
    wind_speed NUMERIC,
    sunshine BOOLEAN,
    PRIMARY KEY (timestamp)
);

CREATE TABLE IF NOT EXISTS raw_traffic (
    timestamp timestamp,
    sensor_id TEXT,
    long TEXT,
    lat TEXT,
    cars_ratio NUMERIC,
    PRIMARY KEY (timestamp)
);