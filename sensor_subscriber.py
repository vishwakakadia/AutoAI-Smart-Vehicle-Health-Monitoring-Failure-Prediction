import paho.mqtt.client as mqtt
import json
import numpy as np
import joblib
import requests

# Load the trained XGBoost model
model = joblib.load("xgb_model.pkl")  

# Flask API endpoint to send predictions
FLASK_API_URL = "http://127.0.0.1:5050/update_data"

# MQTT Broker
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "vehicle/sensor_data"

# Callback when a message is received from MQTT
def on_message(client, userdata, msg):
    try:
        # Parse incoming JSON data
        data = json.loads(msg.payload.decode())
        
        # Extract sensor values
        features = np.array([
            data["engine_temp"],
            data["battery_voltage"],
            data["fuel_pressure"],
            data["oil_temp"],
            data["engine_load"]
        ]).reshape(1, -1)

        # Run the prediction
        prediction = model.predict(features)[0]  # 0 = Normal, 1 = Failure

        # Add prediction to data
        data["failure_status"] = int(prediction)

        # Send data to Flask API for dashboard
        requests.post(FLASK_API_URL, json=data)

        print(f"Received Data: {data}")

    except Exception as e:
        print(f"Error processing message: {e}")

# MQTT Client Setup
client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)

print("MQTT Subscriber Running...")
client.loop_forever()
