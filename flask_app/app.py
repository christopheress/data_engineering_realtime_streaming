import json
import random
from datetime import datetime

import scipy.stats as stats
from flask import Flask, json

app = Flask(__name__)


@app.route('/weatherdata/')
def get_weatherdata():

    data = {
        'sensor_id': str(random.randint(1, 100)),
        'timestamp': int(datetime.now().timestamp() * 1000),
        'temperature': stats.norm.rvs(loc=15, scale=10, size=1)[0],
        'air_humidity': round(random.uniform(100.0, 0.0), 2),
        'wind_speed': round(random.uniform(80.0, 0.0), 2),
        'sunshine': random.choice([True, False])
    }

    response = app.response_class(
        response=json.dumps(data, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/trafficdata/')
def get_trafficdata():

    data = {
        'sensor_id': str(random.randint(101, 200)),
        'timestamp': int(datetime.now().timestamp() * 1000),
        'long': str(random.randint(1, 100)),
        'lat': str(random.randint(1, 100)),
        'cars_ratio': round(random.uniform(0, 1), 2)
    }

    response = app.response_class(
        response=json.dumps(data, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3030')
