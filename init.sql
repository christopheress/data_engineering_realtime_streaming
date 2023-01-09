CREATE TABLE IF NOT EXISTS raw_weather (
    timestamp TIMESTAMP,
    sensor_id TEXT,
    temperature NUMERIC,
    air_humidity NUMERIC,
    wind_speed NUMERIC,
    sunshine BOOLEAN
);

CREATE TABLE IF NOT EXISTS raw_traffic (
    timestamp TIMESTAMP,
    sensor_id TEXT,
    long TEXT,
    lat TEXT,
    cars_ratio NUMERIC
);

/*CREATE TABLE IF NOT EXISTS stream_weather (
    column1 datatype,
    column2 datatype,
    column3 datatype
);

CREATE TABLE IF NOT EXISTS stream_traffic (
    column1 datatype,
    column2 datatype,
    column3 datatype
);*/