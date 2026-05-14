# 📊 Retail Sales Forecasting & Inventory Optimization System

## 🚀 Project Overview
The Retail Sales Forecasting & Inventory Optimization System is an end-to-end Data Science project designed to help retail businesses forecast future product demand and optimize inventory decisions.

This system uses Machine Learning and Retail Analytics concepts to:
- Predict future sales
- Optimize inventory levels
- Reduce stockouts
- Avoid overstock situations
- Improve profitability

The project simulates how modern retail companies like Amazon, Flipkart, Reliance Retail, Walmart, and D-Mart use forecasting systems for demand planning and inventory management.

---

# 🎯 Problem Statement

Retail businesses often struggle with:

- ❌ Stockouts → Lost sales and unhappy customers
- ❌ Overstocking → Increased holding costs
- ❌ Poor demand planning
- ❌ Inefficient inventory management

This project solves these issues using:
- 📈 Sales Forecasting
- 📦 Inventory Optimization
- 📊 Business Intelligence Dashboard

---

# 💡 Key Features

## 📈 Sales Forecasting
- Predict future product sales using Machine Learning
- Identify demand trends and seasonality

## 📦 Inventory Optimization
- Safety Stock Calculation
- Reorder Point Calculation
- Inventory Recommendation System

## 📊 Dashboard & Analytics
- Interactive Streamlit Dashboard
- Multi-SKU Comparison
- Trend Analysis
- Profit Estimation
- Downloadable CSV Reports

## 🧠 Advanced Concepts
- Feature Engineering
- Lag Features
- Rolling Mean Analysis
- Croston Method for Intermittent Demand

---

# 🛠️ Tech Stack

| Category | Tools/Libraries |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Dashboard | Streamlit |
| Forecasting | Random Forest |
| Version Control | Git & GitHub |

---

# 🏗️ Project Architecture

```text
Retail Data
     ↓
Data Cleaning & Preprocessing
     ↓
Feature Engineering
     ↓
Machine Learning Forecasting
     ↓
Inventory Optimization Logic
     ↓
Forecast & Inventory Outputs
     ↓
Interactive Dashboard

📂 Folder Structure

Retail-Sales-Forecasting-Inventory-Optimization/
│
├── data/
│   └── retail_data.csv
│
├── src/
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── croston.py
│   └── inventory.py
│
├── app/
│   └── app.py
│
├── outputs/
│   ├── forecast.csv
│   └── inventory.csv
│
├── images/
│   ├── dashboard.png
│   ├── graph.png
│   └── inventory.png
│
├── create_dataset.py
├── main.py
├── requirements.txt
└── README.md

▶️ How to Run the Project

Step 1: Generate Dataset
python create_dataset.py

Step 2: Train Model & Generate Outputs
python main.py

Step 3: Launch Dashboard
python -m streamlit run app/app.py

📊 Dashboard Features

Product Selection
Store Selection
Sales vs Forecast Graph
Inventory Recommendation Table
Trend Analysis
Profit Estimation
CSV Download Button
