import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# File paths
input_file_path = 'Input_X.xlsx'  # Replace with your input file path
output_file_path = 'Output_Y.xlsx'  # Replace with your output file path
model_file_path = 'svm_model_tuned.pkl'  # Model saved from the development code
# scaler_file_path = 'scaler.pkl'  # Scaler saved from the development code

# Load the input and actual output files
input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)
y_actual = output_data['CHL_a']

# Load the saved model
svm_model = joblib.load(model_file_path)

# Load and apply the scaler to the input data
scaler = StandardScaler()
input_data_scaled = scaler.fit_transform(input_data)

# Predict on the entire dataset
y_pred_log = svm_model.predict(input_data_scaled)

# Transform predictions back to the original scale
y_pred = np.expm1(y_pred_log)

# Save the results to an Excel file
results = pd.DataFrame({'Actual': y_actual, 'Predicted': y_pred})
results.to_excel('prediction_results_svm_tuned.xlsx', index=False)

# Calculate global axis limits
min_value = min(y_actual.min(), y_pred.min())
max_value = max(y_actual.max(), y_pred.max())

# Plot scatter plot for actual vs predicted values
plt.figure(figsize=(8, 6))
plt.scatter(y_actual, y_pred, alpha=0.5, color='purple')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted (Log Scale)')
plt.grid()

# Add identity line
identity_line = np.linspace(min_value, max_value, 100)
plt.plot(identity_line, identity_line, color='red', linestyle='--', label='Identity Line')

# Save the plot as a PNG file
plt.tight_layout()
plt.savefig('svm_prediction_scatter_plot_with_identity_line.png')
plt.show()
