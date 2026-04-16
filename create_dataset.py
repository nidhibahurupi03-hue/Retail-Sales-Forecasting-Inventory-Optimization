import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2022-01-01", end="2023-12-31")
products = ['P1','P2','P3']
stores = ['S1','S2']

data = []

for date in dates:
    for p in products:
        for s in stores:
            base = 20
            
            if date.weekday() >= 5:
                base += 10
            
            sales = max(0, int(base + np.random.normal(0,5)))
            
            data.append([date, p, s, sales])

df = pd.DataFrame(data, columns=["date","product","store","sales"])

df.to_csv("data/retail_data.csv", index=False)

print("Dataset created!")