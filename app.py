from flask import Flask, request, jsonify, render_template
from collections import deque

app = Flask(__name__)

# Store last 100 sensor readings
sensor_data = deque(maxlen=100)

@app.route('/update_data', methods=['POST'])
def update_data():
    data = request.get_json()
    sensor_data.append(data)
    return jsonify({"message": "Data received"}), 200

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(list(sensor_data))

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port = 5050)
