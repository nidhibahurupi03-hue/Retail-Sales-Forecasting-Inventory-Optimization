from src.data_loader import load_data
from src.feature_engineering import create_features
from src.model import train_model, predict
from src.inventory import calculate_inventory

# Load data
df = load_data("data/retail_data.csv")

# Feature engineering
df = create_features(df)

# Train model
model = train_model(df)

# Predict
df['forecast'] = predict(model, df)

# Inventory optimization
inventory = calculate_inventory(df)

# Save outputs
df.to_csv("outputs/forecast.csv", index=False)
inventory.to_csv("outputs/inventory.csv", index=False)

print("Project completed successfully!")