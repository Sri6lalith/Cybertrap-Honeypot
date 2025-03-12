import pandas as pd
import joblib
from scapy.all import sniff, IP, TCP, UDP
import time
import os

# Load trained anomaly detection model (if available)
MODEL_FILE = "/home/ubuntu/isolation_forest_model.pkl"
if os.path.exists(MODEL_FILE):
    model = joblib.load(MODEL_FILE)
else:
    model = None  # If model is missing, anomaly detection won't run

# Define log file
LOG_FILE = "/home/ubuntu/attack_logs.csv"

# Define column headers
COLUMNS = ["timestamp", "src_ip", "dst_ip", "protocol", "length", "src_port", "dst_port", "anomaly"]

# Function to process packets and append them to the CSV
def packet_callback(packet):
    if IP in packet:
        data = {
            "timestamp": time.time(),
            "src_ip": packet[IP].src,
            "dst_ip": packet[IP].dst,
            "protocol": packet[IP].proto,
            "length": len(packet),
            "src_port": packet[TCP].sport if TCP in packet else (packet[UDP].sport if UDP in packet else None),
            "dst_port": packet[TCP].dport if TCP in packet else (packet[UDP].dport if UDP in packet else None),
        }
        
        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Predict anomaly if model exists
        if model:
            df_for_model = df.drop(["timestamp", "src_ip", "dst_ip"], axis=1).fillna(0)
            anomaly_score = model.predict(df_for_model)[0]
            df["anomaly"] = "Yes" if anomaly_score == -1 else "No"
        else:
            df["anomaly"] = "Unknown"

        # Append data to CSV (create file if missing)
        file_exists = os.path.isfile(LOG_FILE)
        df.to_csv(LOG_FILE, mode="a", header=not file_exists, index=False)

        print(f"✅ Logged Packet: {data} (Anomaly: {df['anomaly'].values[0]})")

# Start **continuous** sniffing
print("🚀 Capturing real-time network traffic with anomaly detection...")
sniff(prn=packet_callback, store=False, filter="ip")  # No packet limit

