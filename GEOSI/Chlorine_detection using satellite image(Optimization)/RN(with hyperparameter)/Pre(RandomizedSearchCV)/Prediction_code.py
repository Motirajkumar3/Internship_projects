import pandas as pd
import matplotlib.pyplot as plt
import joblib
import numpy as np

# Load the saved hyperparameter-tuned model
model_path = 'random_forest_model_tuned.pkl'  # Replace with your tuned model file path
rf_model = joblib.load(model_path)

# Load the whole dataset
input_file_path = 'Input_X.xlsx'  # Replace with your file path
output_file_path = 'Output_Y.xlsx'  # Replace with your file path

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)
X = input_data
y_actual = output_data['CHL_a']

# Predict on the entire dataset
y_predicted = rf_model.predict(X)

# Save the results to an Excel file
results = pd.DataFrame({'Actual': y_actual, 'Predicted': y_predicted})
results.to_excel('Prediction_Results_Tuned.xlsx', index=False)

# Find axis limits for scatter plot
min_value = min(y_actual.min(), y_predicted.min())
max_value = max(y_actual.max(), y_predicted.max())

# Create scatter plot for the entire dataset
plt.figure(figsize=(8, 8))
plt.scatter(y_actual, y_predicted, alpha=0.5, color='purple')
plt.plot([min_value, max_value], [min_value, max_value], color='black')  # Identity line
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted (Log Scale)')
plt.grid()
plt.savefig('Prediction_Scatter_Plot_Tuned.png', format='png')
plt.show()
