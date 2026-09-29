# 🌦️ Weather App using OpenWeather API

A Python-based command-line weather application that fetches real-time weather information and weather forecasts for any city using the OpenWeather REST API.

## 🚀 Features

- 🌡️ Get current temperature
- 🤗 Get feels-like temperature
- 💧 Display humidity
- ☁️ Display weather condition
- 💨 Display wind speed
- 📅 Get weather forecast
- 🌍 Search weather by city name
- ❌ Handles invalid city names
- 🔐 Secure API key management using `.env`
- ⚠️ Handles API and connection errors
- 🖥️ Simple and beginner-friendly CLI interface

## 🛠️ Technologies Used

- Python
- Requests
- OpenWeather REST API
- JSON
- python-dotenv

## 📁 Project Structure

```text
weather-app-openweather/
│
├── weather.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

> **Note:** `.env` is used only on the local system and is NOT uploaded to GitHub because it contains the API key.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/machadoanish27-ops/weather-app-openweather.git
```

### 2. Open the Project Folder

```bash
cd weather-app-openweather
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

## 🔑 API Key Setup

This project uses the OpenWeather API.

Create a `.env` file inside the project folder and add:

```env
OPENWEATHER_API_KEY=YOUR_API_KEY_HERE
```

Replace `YOUR_API_KEY_HERE` with your own OpenWeather API key.

### ⚠️ Important

Never upload your `.env` file or API key to GitHub.

The `.gitignore` file prevents the `.env` file from being tracked by Git.

## ▶️ Running the Application

Run the following command:

```bash
python weather.py
```

The application will display:

```text
====================================
          LIVE WEATHER APP
====================================
1. Current Weather
2. Weather Forecast
3. Exit
```

### Current Weather

Select:

```text
1
```

Then enter a city name, for example:

```text
Mumbai
```

The application displays:

- City
- Temperature
- Feels-like temperature
- Humidity
- Weather condition
- Wind speed

### Weather Forecast

Select:

```text
2
```

Then enter a city name.

The application displays upcoming forecast information including:

- Date and time
- Temperature
- Humidity
- Weather condition

## 🔒 Security

The OpenWeather API key is stored in a `.env` file instead of being written directly inside the Python source code.

The `.gitignore` file contains:

```text
.env
__pycache__/
```

This prevents sensitive information from being accidentally uploaded to GitHub.

## 🧪 Error Handling

The application handles common errors such as:

- Invalid API key
- City not found
- Network/connection errors
- Empty city input
- API request errors

## 🎯 Learning Outcomes

This project demonstrates practical usage of:

- Python functions
- Loops and conditional statements
- User input handling
- REST API integration
- HTTP requests using `requests`
- JSON response parsing
- Environment variables
- Exception handling
- Basic CLI application development

## 👨‍💻 Author

**Anish Machado**

GitHub:  
https://github.com/machadoanish27-ops

## 📄 License

This project was created for educational and internship purposes.
