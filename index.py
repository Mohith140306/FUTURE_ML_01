import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# 1. LOAD DATA
# Ensure 'Walmart.csv' is in the same folder as this script
df = pd.read_csv('Walmart.csv')

# 2. DATA PREPROCESSING
# Converting Date to datetime (format is DD-MM-YYYY in your file)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df = df.sort_values('Date')

# Feature Engineering: Extracting time-based components
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Week'] = df['Date'].dt.isocalendar().week.astype(int)
df['Day'] = df['Date'].dt.day

# 3. PREPARING FOR MACHINE LEARNING
# We use all features except 'Weekly_Sales' and 'Date'
X = df.drop(['Weekly_Sales', 'Date'], axis=1)
y = df['Weekly_Sales']

# Time-based split: Use the first 80% for training and last 20% for testing
split_index = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split_index], X.iloc[split_index:]
y_train, y_test = y.iloc[:split_index], y.iloc[split_index:]
test_dates = df['Date'].iloc[split_index:]

# 4. BUILDING THE MODEL
print("Training the Random Forest Regressor... please wait.")
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# 5. GENERATING PREDICTIONS & EVALUATION
y_pred = model.predict(X_test)

print("\n--- Model Performance ---")
print(f"Mean Absolute Error (MAE): ${mean_absolute_error(y_test, y_pred):,.2f}")
print(f"R-squared (Accuracy) Score: {r2_score(y_test, y_pred):.4f}")

# 6. BUSINESS VISUALIZATION
# To show a clear trend, we aggregate results by Date (Average across all stores)
test_results = pd.DataFrame({
    'Date': test_dates,
    'Actual': y_test,
    'Predicted': y_pred
})
agg_results = test_results.groupby('Date').mean().reset_index()

plt.figure(figsize=(15, 7))
plt.plot(agg_results['Date'], agg_results['Actual'], label='Actual Sales (History)', color='blue', marker='o', markersize=4)
plt.plot(agg_results['Date'], agg_results['Predicted'], label='Forecasted Sales (Model)', color='red', linestyle='--', marker='x', markersize=4)

plt.title('Walmart Sales Forecast: Actual vs Predicted Trend', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Average Weekly Sales ($)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_forecast_plot.png')
print("\nPlot saved as 'sales_forecast_plot.png'.")

# Export results for documentation
test_results.to_csv('forecast_results.csv', index=False)
print("Forecast results exported to 'forecast_results.csv'.")