import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load data (if it exists)
LOG_FILE = "/home/ubuntu/attack_logs.csv"

try:
    df = pd.read_csv(LOG_FILE)
    df = df[["protocol", "length", "src_port", "dst_port"]].fillna(0)  # Use numerical columns
except FileNotFoundError:
    print("❌ No attack logs found. Train the model after capturing some data.")
    exit()

# Train Isolation Forest Model
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(df)

# Save the trained model
joblib.dump(model, "/home/ubuntu/isolation_forest_model.pkl")
print("✅ Model trained and saved as isolation_forest_model.pkl")
