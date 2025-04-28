# AutoAI-Smart-Vehicle-Health-Monitoring-Failure-Prediction
AutoAI is an AI-driven system designed to monitor vehicle health and predict potential failures in real-time. By leveraging machine learning models and MQTT-based sensor data streaming, it aims to provide proactive maintenance solutions for vehicles.

## Features

- **Real-Time Sensor Data Streaming**: Utilizes MQTT protocol to publish and subscribe to live vehicle sensor data.
- **Predictive Maintenance**: Employs a trained XGBoost model to forecast potential component failures.
- **Interactive Web Interface**: Provides a user-friendly dashboard for monitoring vehicle health and predictions.
- **Data Analysis & Visualization**: Includes exploratory data analysis (EDA) notebooks for in-depth data insights.

## Machine Learning Model

- **Algorithm**: XGBoost Classifier
- **Training Data**: `real_time_sensor_data.csv` containing various sensor readings.
- **Model File**: `xgb_model.pkl` (pre-trained model ready for deployment)

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/vishwakakadia/AutoAI-Smart-Vehicle-Health-Monitoring-Failure-Prediction.git
   cd AutoAI-Smart-Vehicle-Health-Monitoring-Failure-Prediction

2. **Set Up Python Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows

3. **Install Python Dependencies**:

   ```bash
   pip install -r requirements.txt

4. **Simulate Sensor Data with MQTT Publisher & Subscriber**:

   ```bash
   python sensor_publisher.py
   python sensor_subscriber.py

5. **Launch the Flask Web Application**:

   ```bash
   python app.py

6. **Train or Retrain the Machine Learning Model(if required)**
   - model.ipynb


