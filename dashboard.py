import streamlit as st
import pandas as pd
import plotly.express as px
import time

LOG_FILE = "/home/ubuntu/attack_logs.csv"

st.set_page_config(page_title="Cybertrap Dashboard", layout="wide")

st.title("🛡️ Cybertrap: Intrusion Detection Dashboard")

# Auto-refresh every 5 seconds
while True:
    try:
        df = pd.read_csv(LOG_FILE)
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit='s')
    except FileNotFoundError:
        st.error("No attack logs found!")
        df = pd.DataFrame(columns=["timestamp", "src_ip", "dst_ip", "protocol", "length", "src_port", "dst_port", "anomaly"])

    # Show attack statistics
    st.subheader("📊 Attack Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Packets", len(df))
    col2.metric("Unique Source IPs", df["src_ip"].nunique())
    col3.metric("Unique Destination IPs", df["dst_ip"].nunique())

    # Graph 1: Packet Activity Over Time
    st.subheader("📈 Packet Activity Over Time")
    fig1 = px.line(df, x="timestamp", y="length", title="Packet Size Over Time")
    st.plotly_chart(fig1, use_container_width=True)

    # Graph 2: Top Source IPs
    st.subheader("🌍 Top Attacking Source IPs")
    top_src_ips = df["src_ip"].value_counts().head(10)
    fig2 = px.bar(x=top_src_ips.index, y=top_src_ips.values, title="Top 10 Source IPs", labels={'x': 'IP Address', 'y': 'Count'})
    st.plotly_chart(fig2, use_container_width=True)

    # Graph 3: Anomaly Detection
    st.subheader("🚨 Detected Anomalies")
    anomalies = df[df["anomaly"] == "Yes"]
    fig3 = px.scatter(anomalies, x="timestamp", y="length", color="src_ip", title="Anomalies Over Time")
    st.plotly_chart(fig3, use_container_width=True)

    st.write("🔄 **Dashboard auto-refreshes every 5 seconds**")
    
    time.sleep(5)  # Refresh every 5 seconds
