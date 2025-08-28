import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import mean_squared_error, r2_score

# Load the saved model
model_path = 'optimized_random_forest_model.pkl'  # Path to the saved model
rf_model = joblib.load(model_path)

# Load the dataset (both input and output files)
input_file_path = 'Input_X.xlsx'  # Replace with your file path
output_file_path = 'Output_Y.xlsx'  # Replace with your file path

X = pd.read_excel(input_file_path)
y_actual = pd.read_excel(output_file_path)['CHL_a']

# Predict the output for the entire dataset
y_pred = rf_model.predict(X)

# Metrics for the entire dataset
mse = mean_squared_error(y_actual, y_pred)
r2 = r2_score(y_actual, y_pred)

print(f"Prediction Results:")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R² Score: {r2:.4f}")

# Save the results to an Excel file
results = pd.DataFrame({'Actual': y_actual, 'Predicted': y_pred})
results.to_excel('Prediction_Results.xlsx', index=False)
print("Prediction results saved to 'Prediction_Results.xlsx'.")

# Find axis limits for scatter plot
min_value = min(y_actual.min(), y_pred.min())
max_value = max(y_actual.max(), y_pred.max())

# Scatter Plot: Actual vs Predicted with Identity Line
plt.figure(figsize=(8, 8))
plt.scatter(y_actual, y_pred, alpha=0.5, color='purple', label='Predictions')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--', linewidth=2, label='Identity Line')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted with Identity Line (Log Scale)')
plt.legend()
plt.grid()

# Save the scatter plot
plt.savefig('Prediction_Scatter_Plot.png', format='png')
plt.show()
print("Scatter plot saved to 'Prediction_Scatter_Plot.png'.")
