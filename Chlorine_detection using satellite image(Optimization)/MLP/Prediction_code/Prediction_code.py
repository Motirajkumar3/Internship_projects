import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load the saved model
model = joblib.load('MLP_Model.pkl')

# Load the entire dataset
input_file_path = 'Input_X.xlsx'  
output_file_path = 'Output_Y.xlsx'  

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)

# Predict outputs for the entire dataset
y_actual = output_data['CHL_a']
y_pred = model.predict(input_data)

# Save results to Excel
results = pd.DataFrame({'Actual': y_actual, 'Predicted': y_pred})
results.to_excel('Prediction_Results.xlsx', index=False)

# Create scatter plot for the entire dataset
min_value = min(min(y_actual), min(y_pred))
max_value = max(max(y_actual), max(y_pred))*3

plt.figure(figsize=(8, 6))
plt.scatter(y_actual, y_pred, alpha=0.5, color='purple')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted - Full Dataset')
plt.grid()
plt.plot([min_value, max_value], [min_value, max_value], color='black',linewidth=1.5, label='1:1 Line')

plt.savefig('Scatter_Plot_Full_Dataset.png')
plt.show()
