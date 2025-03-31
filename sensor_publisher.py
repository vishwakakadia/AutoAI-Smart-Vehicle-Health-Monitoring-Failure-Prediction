import time
import random
import json
import paho.mqtt.client as mqtt

# MQTT Broker (HiveMQ - Free Public Broker)
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "vehicle/sensor_data"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT, 60)

# Function to Simulate IoT Vehicle Sensors
def generate_sensor_data():
    
        # "engine_temp": round(random.uniform(70, 120), 2),  # °C
        # "battery_voltage": round(random.uniform(12, 15), 2),  # V
        # "fuel_pressure": round(random.uniform(30, 60), 2),  # PSI
        # "oil_temp": round(random.uniform(80, 150), 2),  # °C
        # "engine_load": round(random.uniform(20, 80), 2)  # %
    engine_temp = round(random.uniform(70, 120) + random.uniform(-2, 2), 2)  # °C with noise between -2 and 2
    battery_voltage = round(random.uniform(12, 15) + random.uniform(-0.1, 0.1), 2)  # V with noise between -0.1 and 0.1
    fuel_pressure = round(random.uniform(30, 60) + random.uniform(-1, 1), 2)  # PSI with noise between -1 and 1
    oil_temp = round(random.uniform(80, 150) + random.uniform(-3, 3), 2)  # °C with noise between -3 and 3
    engine_load = round(random.uniform(20, 80) + random.uniform(-5, 5), 2)  # % with noise between -5 and 5
    return{
        "engine_temp": engine_temp,
        "battery_voltage": battery_voltage,
        "fuel_pressure": fuel_pressure,
        "oil_temp": oil_temp,
        "engine_load": engine_load
    }

# Continuous Data Streaming
while True:
    data = generate_sensor_data()
    json_data = json.dumps(data)
    client.publish(TOPIC, json_data)
    print(f"Sent Data: {json_data}")
    time.sleep(2)  # Send data every 2 seconds
