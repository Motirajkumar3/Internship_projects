import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load the saved model
gp_model = joblib.load('GP_Model_Optimized.pkl')

# Load the full dataset
input_file_path = 'Input_X.xlsx'
output_file_path = 'Output_Y.xlsx'

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)
X = input_data
y_actual = output_data['CHL_a']

# Predict using the loaded model
y_pred = gp_model.predict(X)

# Save the results
results = pd.DataFrame({'Actual': y_actual, 'Predicted': y_pred})
results.to_excel('Full_Dataset_Predictions_Optimized.xlsx', index=False)

# Plot scatterplot for actual vs predicted
plt.figure(figsize=(6, 6))

# Determine axis limits for identity line
min_value = min(y_actual.min(), y_pred.min())
max_value = max(y_actual.max(), y_pred.max())

# Scatter plot
plt.scatter(y_actual, y_pred, alpha=0.5, color='purple', label='Data Points')
plt.plot([min_value, max_value], [min_value, max_value], color='black', label='Identity Line')  # Identity line
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted (Full Dataset)')
plt.legend()
plt.grid()

# Save and show the plot
plt.tight_layout()
plt.savefig('Full_Dataset_Scatter_Identity_Line.png')
plt.show()
