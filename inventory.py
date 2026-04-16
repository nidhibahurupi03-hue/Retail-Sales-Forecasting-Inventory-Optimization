import numpy as np
import pandas as pd
from scipy.stats import norm

def calculate_inventory(df):
    
    results = []
    
    for (p,s), group in df.groupby(['product','store']):
        
        forecast = group['forecast'].iloc[-7:].mean()
        lead_time = 7
        
        std = group['sales'].std()
        
        z = norm.ppf(0.95)
        
        safety_stock = z * std * np.sqrt(lead_time)
        reorder_point = forecast * lead_time + safety_stock
        
        order_qty = max(0, reorder_point - forecast)
        
        results.append({
            "product": p,
            "store": s,
            "forecast": forecast,
            "safety_stock": safety_stock,
            "reorder_point": reorder_point,
            "order_quantity": order_qty
        })
    
    return pd.DataFrame(results)