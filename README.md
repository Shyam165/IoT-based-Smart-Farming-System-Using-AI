# AI-Based Smart Farming System
## Table of Contents
•	Introduction
•	Features
•	Requirements
•	Installation
•	Usage
•	IoT Integration
•	Demo
•	Contributing
•	License
## Introduction
This project is an AI-based smart farming system that predicts suitable crops for a given set of environmental factors (temperature, humidity, pH value, potassium, nitrogen, phosphorus, rainfall level) and also offers plant disease prediction for scabs percentage in plants. It is designed to assist farmers in making informed decisions about crop selection and disease management.
The system is built as a web application using the Streamlit library and has future plans for IoT integration. The project also utilizes Adafruit IO for cloud-based sensor data analysis and irrigation system control based on soil moisture values.
## Features
•	Crop recommendation based on environmental factors.
•	Plant disease prediction (scabs percentage).
•	User-friendly web application interface.
•	Future-ready for IoT sensor integration.
•	Cloud-based sensor data analysis using Adafruit IO.
•	Manual and automatic irrigation control based on soil moisture.
## Requirements
Before you begin, ensure you have met the following requirements:
•	Python 3.x
•	Required Python packages (list them and provide installation instructions).
•	Adafruit IO account for cloud-based sensor data analysis.
•	IoT sensors (DHT11, DS18B20, soil moisture sensor, soil NPK sensor, pH sensor).
## Installation
1.	Clone the repository:
git clone https://github.com/yourusername/your-repo.git cd your-repo 
2.	Install the required Python packages:
pip install -r requirements.txt 
3.	Create an Adafruit IO account and configure the necessary credentials.
4.	Connect and set up your IoT sensors.
## Usage
1.	Run the application:
streamlit run app.py 
2.	Input environmental factors (temperature, humidity, pH value, etc.) and get crop recommendations.
3.	Use the plant disease prediction feature to assess the scabs percentage in plants.
4.	For IoT integration, follow the instructions in the IoT Integration section.
## IoT Integration
1.	Connect and configure your IoT sensors (DHT11, DS18B20, soil moisture sensor, soil NPK sensor, pH sensor).
2.	Create a project on Adafruit IO and set up feeds for your sensors.
3.	Use the Adafruit IO interface to analyze and understand the data from your sensors on the cloud.
4.	Implement manual or automatic irrigation control based on soil moisture values through Adafruit IO.
## Demo
Provide a link or description of how to access a live demo of your smart farming system.
## Contributing
1.	Fork the repository.
2.	Create a new branch.
3.	Make your contributions.
4.	Submit a pull request.
## License
This project is licensed under the [License Name] - see the LICENSE file for details.
