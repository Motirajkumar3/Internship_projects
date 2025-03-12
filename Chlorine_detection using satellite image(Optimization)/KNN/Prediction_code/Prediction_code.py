import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import joblib  # For loading the model

# Load the input and output files
input_file_path = 'Input_X.xlsx'  # Replace with your file path
output_file_path = 'Output_Y.xlsx'  # Replace with your file path

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)

# Load the saved model
knn_model = joblib.load('KNN_Model.pkl')

# Predict on the entire dataset
y_pred = knn_model.predict(input_data)

# Save the results to Excel
results = pd.DataFrame({'Actual': output_data['CHL_a'], 'Predicted': y_pred})
results.to_excel('Prediction_Results.xlsx', index=False)

# Find the axis limits for scatter plot
min_value = min(output_data['CHL_a'].min(), y_pred.min())
max_value = max(output_data['CHL_a'].max(), y_pred.max())

# Scatter plot for actual vs. predicted
plt.figure(figsize=(6, 6))
plt.scatter(output_data['CHL_a'], y_pred, alpha=0.5, color='purple')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted (Log Scale)')
plt.grid()
plt.plot([min_value, max_value], [min_value, max_value], color='black')


# Save the scatter plot
plt.savefig('KNN_Prediction_Scatter.png')
plt.show()
