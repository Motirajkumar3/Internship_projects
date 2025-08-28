import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import joblib

# Load the input and output files
input_file_path = 'Input_X.xlsx'  # Replace with your file path
output_file_path = 'Output_Y.xlsx'  # Replace with your file path

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)

# Split the data into features (X) and target (y)
X = input_data
y = output_data['CHL_a']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predict on training and testing datasets
y_train_pred = rf_model.predict(X_train)
y_test_pred = rf_model.predict(X_test)

# Save training and testing results to Excel files
train_results = pd.DataFrame({'Actual': y_train, 'Predicted': y_train_pred})
test_results = pd.DataFrame({'Actual': y_test, 'Predicted': y_test_pred})
train_results.to_excel('Training_Results.xlsx', index=False)
test_results.to_excel('Testing_Results.xlsx', index=False)

# Save the model
joblib.dump(rf_model, 'random_forest_model.pkl')

# Find axis limits for scatter plots
min_value = min(y_train.min(), y_test.min(), y_train_pred.min(), y_test_pred.min())
max_value = max(y_train.max(), y_test.max(), y_train_pred.max(), y_test_pred.max())

# Create scatter plots
plt.figure(figsize=(12, 6))

# Subplot 1: Training scatter plot
plt.subplot(1, 2, 1)
plt.scatter(y_train, y_train_pred, alpha=0.5, color='blue')
plt.plot([min_value, max_value], [min_value, max_value], color='red', linewidth=1.5)  # 1:1 line
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual (Training)')
plt.ylabel('Predicted (Training)')
plt.title('Training Data: Actual vs Predicted (Log Scale)')
plt.grid()

# Subplot 2: Testing scatter plot
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_test_pred, alpha=0.5, color='green')
plt.plot([min_value, max_value], [min_value, max_value], color='red', linewidth=1.5)  # 1:1 line
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual (Testing)')
plt.ylabel('Predicted (Testing)')
plt.title('Testing Data: Actual vs Predicted (Log Scale)')
plt.grid()

# Save the scatter plots
plt.tight_layout()
plt.savefig('Scatter_Plots_with_1to1.png', format='png')
plt.show()
