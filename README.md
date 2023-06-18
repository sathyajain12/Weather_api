Weather API

The Weather API is a Python Flask application that fetches real-time weather information for a given city using the OpenWeatherMap API. It provides temperature, humidity, wind speed, and other weather details in both Celsius and Fahrenheit.

Installation
------------

1. Clone the repository to your local machine:

   git clone https://github.com/your-username/weather-api.git

2. Navigate to the project directory:

   cd weather-api

3. Install the required dependencies using pip:

   pip install -r requirements.txt

Usage
-----

1. Start the Flask server:

   python main.py

2. Make a GET request to the `/weather/<city>` endpoint, where `<city>` is the name of the city for which you want to fetch weather information.

   Example request: http://localhost:5000/weather/London

   The response will be a JSON object containing the weather details for the specified city.

API Endpoints
--------------

- `/weather/<city>`: Fetches weather information for the specified `<city>`. Returns a JSON response with temperature, humidity, wind speed, and other weather details.

Contributing
------------

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.


