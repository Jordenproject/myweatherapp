import unittest
from app import app  # assuming your Flask app is in app.py

class FlaskAppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This will be run once before all tests
        cls.app = app.test_client()  # Flask test client
        cls.app.testing = True  # Enable testing mode

    def test_forecast_by_city(self):
        # Test /forecast/<city> endpoint
        response = self.app.get('/forecast/London')  # Replace 'London' with a valid city
        self.assertEqual(response.status_code, 200)
        self.assertIn('city', response.json)  # Check that 'city' is in the response
        self.assertIn('temperature', response.json)  # Check that 'temperature' is in the response

    def test_invalid_city(self):
        # Test when an invalid city is provided (simulate error handling)
        response = self.app.get('/forecast/InvalidCity')
        self.assertEqual(response.status_code, 400)  # We expect a Bad Request
        self.assertIn('error', response.json)  # The error message should be present

    def test_compare_daylight(self):
        # Test /compare_daylight/<city1>/<city2> endpoint
        response = self.app.get('/compare_daylight/London/Tokyo')  # Replace with valid cities
        self.assertEqual(response.status_code, 200)
        self.assertIn('city_with_longest_day', response.json)  # Check the response for daylight comparison

    def test_check_rain(self):
        # Test /check_rain/<city1>/<city2> endpoint
        response = self.app.get('/check_rain/London/Tokyo')  # Replace with valid cities
        self.assertEqual(response.status_code, 200)
        self.assertIn('no_rain', response.json)  # Check that the 'no_rain' key exists in the response

    def test_invalid_rain_check(self):
        # Test invalid case for rain check
        response = self.app.get('/check_rain/InvalidCity/Tokyo')
        self.assertEqual(response.status_code, 400)  # Bad request if one city is invalid
        self.assertIn('error', response.json)  # Error should be included in the response

if __name__ == '__main__':
    unittest.main()
