import paho.mqtt.client as mqtt
import json
import pandas as pd

# MQTT Settings
BROKER = "test.mosquitto.org" 
PORT = 1883
TOPIC = "vehicle/sensor_data"
data_list = []

# Debugging function
def on_log(client, userdata, level, buf):
    print(f"MQTT Log: {buf}")  # Shows connection logs

# Fix: Update function signature to accept 'properties'
def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print(f"Connected to MQTT Broker: {BROKER} with result code {rc}")
        client.subscribe(TOPIC)
    else:
        print(f"Failed to connect, return code: {rc}")

# Callback when message is received
def on_message(client, userdata, message):
    data = json.loads(message.payload.decode("utf-8"))
    data_list.append(data)
    print(f"📥 Received Data: {data}")

    if len(data_list) >= 10:
        df = pd.DataFrame(data_list)
        df.to_csv("real_time_sensor_data.csv", mode="a", header=False, index=False)
        print("Data Saved to CSV")
        data_list.clear()

# Fix for MQTT Deprecation Warning
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_log = on_log  # Enable logs
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()
