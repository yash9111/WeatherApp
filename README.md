
# Weather Detector Web App

A Django-based web application that fetches weather data using the OpenWeatherMap API and displays it to users. The app allows users to enter a city name and get real-time weather information for that location.

# Table of Contents
Description

Installation

Usage

Features

Technologies Used

Screenshots

Contributing


# Description

The Weather Detector Web App is a simple yet effective way to check the current weather conditions for any city in the world. It uses the OpenWeatherMap API to fetch real-time weather data, which is then displayed to users in a user-friendly format. The app provides information like temperature, pressure, humidity, and geographical coordinates for the specified city.

# Installation



## Clone the repository:

```bash
$ git clone https://github.com/yash9111/weather-detector-app.git
$ cd weather-detector-app

```
## Install the required packages using pip:

```bash
$ pip install django
```

Obtain an API key from OpenWeatherMap and replace 'YOUR_API_KEY' in views.py with your actual API key.

## Run the development server:
```bash
$ python manage.py runserver
```
Access the app in your web browser at http://127.0.0.1:8000/.



## Usage

Enter the name of a city in the input field and click the "Search" button.
The app will retrieve and display the current weather conditions for the specified city.



## Features

- Real-time weather data fetching using the OpenWeatherMap API.
- Display of temperature in Celsius, pressure in millibars, humidity percentage, and geographical coordinates.
- User-friendly interface for easy interaction.



## Tech Stack

**Django:** Web framework for building the backend of the app.


**OpenWeatherMap API:**  Provides real-time weather data.

**HTML/CSS:** Frontend design and layout.

## Screenshots


![Screenshot 2023-08-10 181631](https://github.com/yash9111/WeatherApp/assets/95490587/dfcc09d7-3ac9-4f6f-9c12-8341a43d1e37)

![Screenshot 2023-08-10 181706](https://github.com/yash9111/WeatherApp/assets/95490587/96b2fd53-b3c3-4e3b-b530-36efe96858fb)

## Contributing

Contributions are welcome! To contribute to the Weather Detector Web App, follow these steps:

- Fork the repository.
- Create a new branch: git checkout -b feature/your-feature.
- Make your changes and commit them: git commit -am 'Add new feature'.
- Push to the branch: git push origin feature/your-feature.
- Create a pull request.

