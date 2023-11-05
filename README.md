# AI-Based Smart Farming System
## Table of Contents
1.	Introduction
2.	Features
3.	Requirements
4.	Installation
5.	Usage
6.	IoT Integration
7.	Demo
8.	Contributing
9.	License
## Introduction
This project is an AI-based smart farming system that predicts suitable crops for a given set of environmental factors (temperature, humidity, pH value, potassium, nitrogen, phosphorus, rainfall level) and also offers plant disease prediction for scabs percentage in plants. It is designed to assist farmers in making informed decisions about crop selection and disease management.
The system is built as a web application using the Streamlit library and has future plans for IoT integration. The project also utilizes Adafruit IO for cloud-based sensor data analysis and irrigation system control based on soil moisture values.
## Templates
### Crop Prediction
![crop prediction](https://github.com/Shyam165/IoT-based-Smart-Farming-System-Using-AI/assets/111563134/83572065-950c-456e-a38d-394b3dc9986d)
### Plant Disease Prediction
![Screenshot 2023-11-05 112500](https://github.com/Shyam165/IoT-based-Smart-Farming-System-Using-AI/assets/111563134/c51174ed-1899-4c68-80be-8db0a9231a92)
### AdaFruit IO Interface: https://io.adafruit.com/YTHOR203/dashboards/piet-at-iotagri
![Screenshot 2023-11-05 113939](https://github.com/Shyam165/IoT-based-Smart-Farming-System-Using-AI/assets/111563134/b667e938-5206-4efe-9f0a-5115b430ec08)

## Features
1.	Crop recommendation based on environmental factors.
2.	Plant disease prediction (scabs percentage).
3.	User-friendly web application interface.
4.	Future-ready for IoT sensor integration.
5.	Cloud-based sensor data analysis using Adafruit IO.
6.	Manual and automatic irrigation control based on soil moisture.
## Requirements
Before you begin, ensure you have met the following requirements:
1.	Python 3.x
2.	Required Python packages (list them and provide installation instructions).
3.	Adafruit IO account for cloud-based sensor data analysis.
4.	IoT sensors (DHT11, DS18B20, soil moisture sensor, soil NPK sensor, pH sensor).
## Installation
1.	Clone the repository:
    git clone https://github.com/Shyam165/IoT-based-Smart-Farming-System-Using-AI.git cd your-repo 
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
So, here is the description of how to access a live demo of our smart farming system: https://agriculturecropprediction-ch9yt2ph6zzvz3et6l23ue.streamlit.app/
## Contributing
1.	Fork the repository.
2.	Create a new branch.
3.	Make your contributions.
4.	Submit a pull request.
## License
This project is licensed under the [License Name] - see the LICENSE file for details.
