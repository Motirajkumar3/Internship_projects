import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import joblib

# Load data
input_file_path = 'Input_X.xlsx'  # Replace with your file path
output_file_path = 'Output_Y.xlsx'  # Replace with your file path

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)

# Split data
X = input_data
y = output_data['CHL_a']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Random Forest with optimal parameters
rf_model = RandomForestRegressor(
    n_estimators=200, max_depth=30, min_samples_split=2, min_samples_leaf=1, random_state=42
)
rf_model.fit(X_train, y_train)

# Predictions
y_train_pred = rf_model.predict(X_train)
y_test_pred = rf_model.predict(X_test)

# Metrics for Training and Testing
mse_train = mean_squared_error(y_train, y_train_pred)
mse_test = mean_squared_error(y_test, y_test_pred)
r2_train = r2_score(y_train, y_train_pred)
r2_test = r2_score(y_test, y_test_pred)

print(f"Training MSE: {mse_train:.4f}, R²: {r2_train:.4f}")
print(f"Testing MSE: {mse_test:.4f}, R²: {r2_test:.4f}")

# Compare Metrics
if abs(r2_train - r2_test) > 0.1 and r2_test < 0.8:
    print("Potential Overfitting: Model performs much better on training data than testing.")
elif r2_train < 0.8 and r2_test < 0.8:
    print("Potential Underfitting: Model performs poorly on both training and testing data.")
else:
    print("Model performs well on both training and testing data.")

# Find axis limits for scatter plots
min_value = min(y_train.min(), y_test.min(), y_train_pred.min(), y_test_pred.min())
max_value = max(y_train.max(), y_test.max(), y_train_pred.max(), y_test_pred.max())

# Scatter Plots for Actual vs Predicted
plt.figure(figsize=(12, 6))

# Training scatter plot
plt.subplot(1, 2, 1)
plt.scatter(y_train, y_train_pred, alpha=0.5, color='blue')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--', linewidth=2)  # Diagonal line
plt.xlabel('Actual (Training)')
plt.ylabel('Predicted (Training)')
plt.title('Training Data: Actual vs Predicted (Log Scale)')
plt.grid()

# Testing scatter plot
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_test_pred, alpha=0.5, color='green')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--', linewidth=2)  # Diagonal line
plt.xlabel('Actual (Testing)')
plt.ylabel('Predicted (Testing)')
plt.title('Testing Data: Actual vs Predicted (Log Scale)')
plt.grid()

# Save the scatter plot
plt.tight_layout()
plt.savefig('Overfitting_Underfitting_Scatter_Plots.png', format='png')
plt.show()
