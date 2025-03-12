# **📖 Setup Guide for Cybertrap Honeypot**

This guide provides **step-by-step instructions** to set up **Cybertrap Honeypot** on **AWS EC2**.

---

## **1️⃣ Setting Up an AWS EC2 Instance**

1. Go to **AWS EC2 Dashboard** → **Launch Instance**
2. Choose **Ubuntu 22.04 LTS**
3. Select **t2.medium** (recommended for performance)
4. Create and download an **SSH key pair**
5. Configure **Security Groups**:
   - **Allow SSH (Port 22)** → Your IP only
   - **Allow HTTP (Port 80)** → `0.0.0.0/0`
   - **Allow Streamlit (Port 8501)** → `0.0.0.0/0`
6. Click **Launch Instance**

---

## **2️⃣ Connecting to EC2**

1. Open a terminal and connect:

```bash
ssh -i ~/.ssh/ec2-key.pem ubuntu@your-ec2-public-ip
```

2. Update & install dependencies:

```bash
sudo apt update && sudo apt install python3-pip -y
pip3 install flask streamlit scikit-learn joblib pandas scapy
```

---

## **3️⃣ Deploying Cybertrap on EC2**

1. Clone the repository:

```bash
git clone https://github.com/Sri6lalith/Cybertrap-Honeypot.git
cd Cybertrap-Honeypot
```

2. Start Packet Sniffer:

```bash
sudo -E python3 packet_sniffer.py
```

3. Start Flask API:

```bash
nohup python3 app.py &
```

4. Start Streamlit Dashboard:

```bash
nohup streamlit run dashboard.py --server.port 8501 --server.enableCORS false --server.enableXsrfProtection false --server.headless true &
```

---

## **4️⃣ Viewing Results**

- **Attack Logs**: `http://your-ec2-public-ip:5000/attacks`
- **Detected Anomalies**: `http://your-ec2-public-ip:5000/anomalies`
- **Live Dashboard**: `http://your-ec2-public-ip:8501`

---

## **📜 Troubleshooting**

If **SSH is not working**, verify:

```bash
chmod 400 ~/.ssh/ec2-key.pem
ssh -i ~/.ssh/ec2-key.pem ubuntu@your-ec2-public-ip
```

If **dashboard is not loading**, check:

```bash
ps aux | grep streamlit
```

Restart Streamlit:

```bash
pkill -f streamlit
nohup streamlit run dashboard.py --server.port 8501 --server.enableCORS false --server.enableXsrfProtection false --server.headless true &
```

---

## **Conclusion**

Now the **Cybertrap Honeypot** is **fully deployed** and **detecting real-time attacks**! 
