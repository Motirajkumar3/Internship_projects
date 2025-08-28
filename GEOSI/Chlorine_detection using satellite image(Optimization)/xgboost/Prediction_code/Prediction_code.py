import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt

# Load the trained model
xg_model = xgb.XGBRegressor()
xg_model.load_model('xgboost_model.json')

# Load the entire dataset
input_file_path = 'Input_X.xlsx'  
output_file_path = 'Output_Y.xlsx' 

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)

X = input_data
y_actual = output_data['CHL_a']

# Predict on the entire dataset
y_pred = xg_model.predict(X)

# Save results to Excel
results = pd.DataFrame({'Actual': y_actual, 'Predicted': y_pred})
results.to_excel('Prediction_Results.xlsx', index=False)

# Find axis limits
min_value = min(y_actual.min(), y_pred.min())
max_value = max(y_actual.max(), y_pred.max())

# Scatter plot for actual vs predicted
plt.figure(figsize=(6, 6))
plt.scatter(y_actual, y_pred, alpha=0.5, color='purple')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted (Log Scale)')
plt.grid()
plt.plot([min_value, max_value], [min_value, max_value], color='black', label='Identity Line')

# Save scatter plot as PNG
plt.tight_layout()
plt.savefig('Scatter_Plot_Whole_Dataset.png')
plt.show()
