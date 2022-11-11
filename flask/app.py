import json
import random
from datetime import datetime
from flask import Flask, json

app = Flask(__name__)


@app.route('/sensordata/<max_sensors>/<number>')
def get_sensor_data(max_sensors, number):
    max_sensors = int(max_sensors)
    number = int(number)

    #data = []
    #loop_range = random.sample(range(1, max_sensors), min(number, max_sensors))
    #for number_sensor in loop_range:
    output_dict = {
        'beach': 'Montrose_Beach',
        'sensor_id': random.randint(1,100), #int(number_sensor)
        'timestamp': "{}".format((datetime.now()).now().isoformat()),
        'water_temperature': round(random.uniform(31.5, 0.0), 2),
        'turbidity': round(random.uniform(1683.48, 0.0), 2),
        'battery_life': round(random.uniform(13.3, 4.8), 2),
        'measurement_id': random.randint(10000, 999999)
    }

    data = output_dict#.append(output_dict)

    response = app.response_class(
        response=json.dumps(data, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3031')
