import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load the saved optimized model
model = joblib.load('Optimized_MLP_Model.pkl')

# Load the entire dataset
input_file_path = 'Input_X.xlsx'  # Replace with your file path
output_file_path = 'Output_Y.xlsx'  # Replace with your file path

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)

# Predict outputs for the entire dataset
y_actual = output_data['CHL_a']
y_pred = model.predict(input_data)

# Save results to Excel
results = pd.DataFrame({'Actual': y_actual, 'Predicted': y_pred})
results.to_excel('Prediction_Results_Optimized.xlsx', index=False)

# Find axis limits for consistent scaling
min_value = min(min(y_actual), min(y_pred))
max_value = max(max(y_actual), max(y_pred))

# Create scatter plots for the predictions
plt.figure(figsize=(12, 6))

# Actual vs Predicted scatter plot
plt.subplot(1, 2, 1)
plt.scatter(y_actual, y_pred, alpha=0.5, color='purple', label='Predicted vs Actual')
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--', linewidth=1.5, label='1:1 Line')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted - Full Dataset')
plt.legend()
plt.grid()

# Residuals plot (Actual - Predicted)
plt.subplot(1, 2, 2)
residuals = y_actual - y_pred
plt.scatter(y_actual, residuals, alpha=0.5, color='orange', label='Residuals')
plt.xscale('log')
plt.xlabel('Actual Values')
plt.ylabel('Residuals (Actual - Predicted)')
plt.title('Residuals vs Actual Values')
plt.axhline(0, color='red', linestyle='--', linewidth=1)  # Add reference line at 0
plt.grid()

plt.tight_layout()
plt.savefig('Optimized_Scatter_Plots_Prediction.png')
plt.show()
