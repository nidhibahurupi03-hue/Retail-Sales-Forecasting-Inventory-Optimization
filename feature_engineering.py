def create_features(df):
    df = df.sort_values('date')
    
    df['lag_1'] = df.groupby(['product','store'])['sales'].shift(1)
    df['lag_7'] = df.groupby(['product','store'])['sales'].shift(7)
    
    df['rolling_mean'] = df.groupby(['product','store'])['sales'].shift(1).rolling(7).mean()
    
    df['day_of_week'] = df['date'].dt.dayofweek
    
    df = df.dropna()
    
    return df