from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

LOG_FILE = "/home/ubuntu/attack_logs.csv"

@app.route('/attacks', methods=['GET'])
def get_attacks():
    try:
        df = pd.read_csv(LOG_FILE)
        return jsonify(df.to_dict(orient="records"))
    except FileNotFoundError:
        return jsonify({"error": "No attack logs found!"})

@app.route('/anomalies', methods=['GET'])
def get_anomalies():
    try:
        df = pd.read_csv(LOG_FILE)
        anomalies = df[df["anomaly"] == "Yes"]
        return jsonify(anomalies.to_dict(orient="records"))
    except FileNotFoundError:
        return jsonify({"error": "No attack logs found!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
