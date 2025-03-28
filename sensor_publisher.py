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
    return {
        "engine_temp": round(random.uniform(70, 120), 2),  # °C
        "battery_voltage": round(random.uniform(12, 15), 2),  # V
        "fuel_pressure": round(random.uniform(30, 60), 2),  # PSI
        "oil_temp": round(random.uniform(80, 150), 2),  # °C
        "engine_load": round(random.uniform(20, 80), 2)  # %
    }

# Continuous Data Streaming
while True:
    data = generate_sensor_data()
    json_data = json.dumps(data)
    client.publish(TOPIC, json_data)
    print(f"🚗 Sent Data: {json_data}")
    time.sleep(2)  # Send data every 2 seconds
