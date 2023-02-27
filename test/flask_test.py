import unittest
from flask_app.app import app
import json

class TestFlask(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True

    def test_get_weatherdata(self):
        response = self.app.get('/weatherdata/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        data = json.loads(response.data)
        self.assertIsInstance(data['sensor_id'], str)
        self.assertIsInstance(data['timestamp'], int)
        self.assertIsInstance(data['temperature'], float)
        self.assertIsInstance(data['air_humidity'], float)
        self.assertIsInstance(data['wind_speed'], float)
        self.assertIsInstance(data['sunshine'], bool)

    def test_get_trafficdata(self):
        response = self.app.get('/trafficdata/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        data = json.loads(response.data)
        self.assertIsInstance(data['sensor_id'], str)
        self.assertIsInstance(data['timestamp'], int)
        self.assertIsInstance(data['long'], str)
        self.assertIsInstance(data['lat'], str)
        self.assertIsInstance(data['cars_ratio'], float)
        self.assertGreaterEqual(data['cars_ratio'], 0)
        self.assertLessEqual(data['cars_ratio'], 1)

if __name__ == '__main__':
    unittest.main()

