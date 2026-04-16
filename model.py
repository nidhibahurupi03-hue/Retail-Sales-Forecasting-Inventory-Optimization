from sklearn.ensemble import RandomForestRegressor

def train_model(df):
    features = ['lag_1','lag_7','rolling_mean','day_of_week']
    
    X = df[features]
    y = df['sales']
    
    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=10,
        random_state=42
    )
    
    model.fit(X, y)
    
    return model

def predict(model, df):
    features = ['lag_1','lag_7','rolling_mean','day_of_week']
    return model.predict(df[features])