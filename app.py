import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="Retail Dashboard", layout="wide")

st.title("📊 Retail Sales Forecasting & Inventory Dashboard")

# Paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
inv_path = os.path.join(base_dir, "outputs", "inventory.csv")
forecast_path = os.path.join(base_dir, "outputs", "forecast.csv")

# Load data
inv_df = pd.read_csv(inv_path)
forecast_df = pd.read_csv(forecast_path)

# Sidebar filters
st.sidebar.header("🔍 Filters")

products = st.sidebar.multiselect(
    "Select Products", 
    inv_df['product'].unique(),
    default=[inv_df['product'].unique()[0]]
)

store = st.sidebar.selectbox("Select Store", inv_df['store'].unique())

# Filter data
filtered_inv = inv_df[(inv_df['product'].isin(products)) & (inv_df['store'] == store)]
filtered_forecast = forecast_df[(forecast_df['product'].isin(products)) & (forecast_df['store'] == store)]

# ==============================
# 📦 INVENTORY TABLE
# ==============================
st.subheader("📦 Inventory Recommendation")
st.dataframe(filtered_inv)

# Download button
csv = filtered_inv.to_csv(index=False).encode('utf-8')
st.download_button(
    "⬇ Download Inventory CSV",
    csv,
    "inventory_output.csv",
    "text/csv"
)

# ==============================
# 📈 MULTIPLE SKU GRAPH
# ==============================
st.subheader("📈 Sales vs Forecast (Multiple SKU)")

plt.figure(figsize=(10,5))

for p in products:
    temp = filtered_forecast[filtered_forecast['product'] == p]
    plt.plot(temp['sales'], label=f"{p} Actual")
    plt.plot(temp['forecast'], linestyle='dashed', label=f"{p} Forecast")

plt.legend()
plt.xlabel("Time")
plt.ylabel("Sales")

st.pyplot(plt)

# ==============================
# 📊 TREND DECOMPOSITION (Simple)
# ==============================
st.subheader("📉 Trend Analysis (Rolling Mean)")

trend = filtered_forecast.groupby('date')['sales'].mean().rolling(7).mean()

plt.figure(figsize=(10,4))
plt.plot(trend, color='blue')
plt.title("7-Day Moving Average Trend")

st.pyplot(plt)

# ==============================
# 💰 PROFIT CALCULATION
# ==============================
st.subheader("💰 Profit Estimation")

# Assume values
price = 100
cost = 60

filtered_inv['estimated_profit'] = (price - cost) * filtered_inv['forecast']

st.dataframe(filtered_inv[['product','store','forecast','estimated_profit']])

# ==============================
# 📊 KPI METRICS
# ==============================
st.subheader("📊 Key Metrics")

if not filtered_inv.empty:
    col1, col2, col3 = st.columns(3)

    col1.metric("Avg Forecast", int(filtered_inv['forecast'].mean()))
    col2.metric("Avg Safety Stock", int(filtered_inv['safety_stock'].mean()))
    col3.metric("Avg Reorder Point", int(filtered_inv['reorder_point'].mean()))