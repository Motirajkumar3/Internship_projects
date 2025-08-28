import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load the saved model
model_path = 'random_forest_model.pkl'  # Replace with your model file path
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
results.to_excel('Prediction_Results.xlsx', index=False)

# Load training predictions
training_results = pd.read_excel('Training_Results.xlsx')
y_train_actual = training_results['Actual']
y_train_predicted = training_results['Predicted']

# Find axis limits for scatter plots
min_value = min(y_actual.min(), y_predicted.min(), y_train_actual.min(), y_train_predicted.min())
max_value = max(y_actual.max(), y_predicted.max(), y_train_actual.max(), y_train_predicted.max())

# Create scatter plots
plt.figure(figsize=(12, 6))

# Subplot 1: Training data scatter plot
plt.subplot(1, 2, 1)
plt.scatter(y_train_actual, y_train_predicted, alpha=0.5, color='blue')
plt.plot([min_value, max_value], [min_value, max_value], color='red', linewidth=1.5)  # 1:1 line
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual (Training)')
plt.ylabel('Predicted (Training)')
plt.title('Training Data: Actual vs Predicted (Log Scale)')
plt.grid()

# Subplot 2: Entire dataset scatter plot
plt.subplot(1, 2, 2)
plt.scatter(y_actual, y_predicted, alpha=0.5, color='purple')
plt.plot([min_value, max_value], [min_value, max_value], color='red', linewidth=1.5)  # 1:1 line
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual (Entire Dataset)')
plt.ylabel('Predicted (Entire Dataset)')
plt.title('Entire Dataset: Actual vs Predicted')
plt.grid()

# Save the scatter plots
plt.tight_layout()
plt.savefig('Prediction_Subplots_with_1to1.png', format='png')
plt.show()
