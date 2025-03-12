import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import joblib  # For saving the model

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

# Initialize and train the KNN model
knn_model = KNeighborsRegressor(n_neighbors=5)  # You can change the number of neighbors
knn_model.fit(X_train, y_train)

# Predict on training and testing datasets
y_train_pred = knn_model.predict(X_train)
y_test_pred = knn_model.predict(X_test)

# Save training results to Excel
training_results = pd.DataFrame({'Actual': y_train, 'Predicted': y_train_pred})
training_results.to_excel('Training_Results.xlsx', index=False)

# Save testing results to Excel
testing_results = pd.DataFrame({'Actual': y_test, 'Predicted': y_test_pred})
testing_results.to_excel('Testing_Results.xlsx', index=False)

# Save the model
joblib.dump(knn_model, 'KNN_Model.pkl')

# Scatter plot for training and testing results
min_value = min(y_train.min(), y_test.min(), y_train_pred.min(), y_test_pred.min())
max_value = max(y_train.max(), y_test.max(), y_train_pred.max(), y_test_pred.max())

plt.figure(figsize=(12, 6))

# Training scatter plot
plt.subplot(1, 2, 1)
plt.scatter(y_train, y_train_pred, alpha=0.5, color='blue')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values (Training)')
plt.ylabel('Predicted Values (Training)')
plt.title('Training Data: Actual vs Predicted (Log Scale)')
plt.grid()
plt.plot([min_value, max_value], [min_value, max_value], color='black')


# Testing scatter plot
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_test_pred, alpha=0.5, color='green')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values (Testing)')
plt.ylabel('Predicted Values (Testing)')
plt.title('Testing Data: Actual vs Predicted (Log Scale)')
plt.grid()
plt.plot([min_value, max_value], [min_value, max_value], color='black')


# Save the scatter plot
plt.tight_layout()
plt.savefig('KNN_Training_Testing_Scatter.png')
plt.show()
