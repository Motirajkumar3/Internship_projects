import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load the data
input_file_path = 'Input_X.xlsx'  # Replace with your file path
output_file_path = 'Output_Y.xlsx'  # Replace with your file path

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)

X = input_data
y = output_data['CHL_a']

# Load the trained model
best_model = joblib.load('Optimized_MLP_Model_Fast.pkl')

# Make predictions
y_pred = best_model.predict(X)

# Save results to Excel
results = pd.DataFrame({'Actual': y, 'Predicted': y_pred})
results.to_excel('Prediction_Results_Fast.xlsx', index=False)

# Find axis limits for consistent scaling
min_value = min(min(y), min(y_pred))
max_value = max(max(y), max(y_pred))

# Create scatter plot for the entire dataset
plt.figure(figsize=(6, 6))
plt.scatter(y, y_pred, alpha=0.5, color='purple', label='Predicted vs Actual')
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--', linewidth=1.5, label='1:1 Line')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Entire Dataset: Actual vs Predicted')
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig('Scatter_Plot_Prediction_Fast.png')
plt.show()
