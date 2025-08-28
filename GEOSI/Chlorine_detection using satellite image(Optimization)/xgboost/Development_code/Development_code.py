import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the input and output files
input_file_path = 'Input_X.xlsx'  
output_file_path = 'Output_Y.xlsx'  

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)

# Split the data into features (X) and target (y)
X = input_data
y = output_data['CHL_a']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the XGBoost model
xg_model = xgb.XGBRegressor(n_estimators=100, random_state=42)
xg_model.fit(X_train, y_train)

# Predictions for training and testing sets
y_train_pred = xg_model.predict(X_train)
y_test_pred = xg_model.predict(X_test)

# Save training results to Excel
train_results = pd.DataFrame({'Actual': y_train, 'Predicted': y_train_pred})
train_results.to_excel('Training_Results.xlsx', index=False)

# Save testing results to Excel
test_results = pd.DataFrame({'Actual': y_test, 'Predicted': y_test_pred})
test_results.to_excel('Testing_Results.xlsx', index=False)

# Save the model to a file
xg_model.save_model('xgboost_model.json')

# Find axis limits
min_value = min(y_train.min(), y_test.min(), y_train_pred.min(), y_test_pred.min())
max_value = max(y_train.max(), y_test.max(), y_train_pred.max(), y_test_pred.max())

# Create scatter plot for training and testing
plt.figure(figsize=(12, 6))

# Training scatter plot
plt.subplot(1, 2, 1)
plt.scatter(y_train, y_train_pred, alpha=0.5, color='red')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values (Training)')
plt.ylabel('Predicted Values (Training)')
plt.title('Actual vs Predicted - Training Data (Log Scale)')
plt.grid()
plt.plot([min_value, max_value], [min_value, max_value], color='black', label='Identity Line')


# Testing scatter plot
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_test_pred, alpha=0.5, color='green')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values (Testing)')
plt.ylabel('Predicted Values (Testing)')
plt.title('Actual vs Predicted - Testing Data (Log Scale)')
plt.grid()
plt.plot([min_value, max_value], [min_value, max_value], color='black', label='Identity Line')


# Save scatter plot as PNG
plt.tight_layout()
plt.savefig('Scatter_Plot_Training_Testing.png')
plt.show()
