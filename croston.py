import numpy as np

def croston_forecast(series, alpha=0.1, periods=7):
    demand = series.values
    
    if np.sum(demand) == 0:
        return np.zeros(periods)
    
    z = demand[demand > 0]
    p = np.diff(np.where(demand > 0)[0])
    
    z_hat = z[0]
    p_hat = p[0] if len(p) > 0 else 1
    
    for i in range(1, len(z)):
        z_hat = alpha*z[i] + (1-alpha)*z_hat
    
    for i in range(1, len(p)):
        p_hat = alpha*p[i] + (1-alpha)*p_hat
    
    forecast = (z_hat / p_hat)
    
    return np.repeat(forecast, periods)