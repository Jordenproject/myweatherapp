# Weather Forecast Flask Application

This Flask application provides weather-related data through a series of API endpoints. It fetches weather information from the **Visual Crossing Weather API** and allows users to query weather forecasts, compare daylight hours, and check if it's raining in two cities.

## Project Structure

- `app.py`: Contains the core logic of the application, with routes and functions for handling weather data.
- `.env`: Stores sensitive environment variables such as the Visual Crossing API key. (Make sure this file is not committed to version control)
- `requirements.txt`: Contains all the Python dependencies required for the project.

## Dependencies

The application requires the following Python libraries:

- **Flask**: A micro web framework for Python.
- **requests**: A library to make HTTP requests to external APIs.
- **python-dotenv**: A library to load environment variables from a `.env` file.

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
Environment Setup
Create a .env file in the root directory with the following content:

env
Copy
VISUAL_CROSSING_API_KEY=your_api_key_here
Explanation of the Code
App Setup
We start by initializing the Flask app and loading environment variables from the .env file.

python
Copy
app = Flask(__name__)
load_dotenv()
API_KEY = os.getenv('VISUAL_CROSSING_API_KEY')
Fetching Weather Data
The get_weather function fetches weather data from the Visual Crossing API for a given city:

python
Copy
def get_weather(city):
    ...
API Routes
Forecast for a City (/forecast/<city>):

Fetches the current temperature and daylight hours for a given city.
Compare Daylight Hours (/compare_daylight/<city1>/<city2>):

Compares the daylight hours between two cities and returns the city with the longest daylight.
Check for Rain (/check_rain/<city1>/<city2>):

Simulates a check for rain by checking if the temperature is below 20°C.
Running the Application
To run the Flask application:

bash
Copy
python app.py
The server will start, and you can access the API through the endpoints mentioned above.

Error Handling
The app provides meaningful error messages for invalid city names, issues with the API response, or other exceptions.
