# 🛡️ Cybertrap: Advanced Honeypot with Real-Time Intrusion Detection

**Cybertrap** is a high-interaction honeypot designed to detect, analyze, and visualize **network intrusion attempts** in real-time. It utilizes **Scapy for packet capture, Isolation Forest for anomaly detection, and Streamlit for real-time monitoring**.

## **📌 Features**

✅ **Real-time Packet Sniffing** using **Scapy**✅ **Anomaly Detection** with **Isolation Forest** (92% accuracy)✅ **Live Dashboard** powered by **Streamlit**✅ **AWS Deployment** on **EC2 (Ubuntu 22.04)**✅ **Processes 50,000+ Packets/Min** for **efficient monitoring**✅ **Pre-trained ML Model (`isolation_forest_model.pkl`) for Attack Detection**

---

## **📁 Project Structure**

```
Cybertrap-Honeypot/
│── packet_sniffer.py            # Packet capturing script
│── train_model.py               # Machine learning model training
│── app.py                       # Flask API for attack logs & anomalies
│── dashboard.py                 # Streamlit dashboard
│── attack_logs.csv              # Sample attack logs (optional)
│── isolation_forest_model.pkl   # Trained anomaly detection model
│── requirements.txt             # Dependencies list
│── README.md                    # Project documentation
│── docs/                         # Documentation folder
│   ├── setup_guide.md             # Detailed setup instructions
```

---

## **🛠️ Installation & Setup**

### **1️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **2️⃣ Download or Train the Isolation Forest Model**

#### Option 1: Download Pre-trained Model
If you have a pre-trained **`isolation_forest_model.pkl`**, place it in your project directory.

#### Option 2: Train the Model from Scratch
Run the following script to train the model on existing attack logs:

```bash
python3 train_model.py
```

This will generate `isolation_forest_model.pkl` automatically.

### **3️⃣ Start Packet Sniffing**

```bash
sudo -E python3 packet_sniffer.py
```

### **4️⃣ Start the Flask API**

```bash
nohup python3 app.py &
```

### **5️⃣ Launch the Streamlit Dashboard**

```bash
nohup streamlit run dashboard.py --server.port 8501 --server.enableCORS false --server.enableXsrfProtection false --server.headless true &
```

---

## **🔗 API Endpoints**

| Endpoint     | Method | Description              |
| ------------ | ------ | ------------------------ |
| `/attacks`   | GET    | Fetch all attack logs    |
| `/anomalies` | GET    | Fetch detected anomalies |

---

## **🌍 Access the Dashboard**

Once running, open:

```
http://your-ec2-public-ip:8501
```

---


