import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import joblib

# Load the data
input_file_path = 'Input_X.xlsx'  # Replace with your file path
output_file_path = 'Output_Y.xlsx'  # Replace with your file path

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)

# Split the data
X = input_data
y = output_data['CHL_a']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model
mlp = MLPRegressor(random_state=42)

# Define the hyperparameter grid
param_grid = {
    'hidden_layer_sizes': [(50,), (100,), (100, 50)],
    'activation': ['relu', 'tanh'],
    'solver': ['adam', 'sgd'],
    'learning_rate': ['constant', 'adaptive'],
    'alpha': [0.0001, 0.001, 0.01]  # L2 regularization parameter
}

# Perform GridSearchCV
grid_search = GridSearchCV(estimator=mlp, param_grid=param_grid, scoring='neg_mean_squared_error', cv=3, verbose=2)
grid_search.fit(X_train, y_train)

# Retrieve the best model and hyperparameters
best_model = grid_search.best_estimator_
best_params = grid_search.best_params_

print("Best Hyperparameters:", best_params)

# Predict using the best model
y_train_pred = best_model.predict(X_train)
y_test_pred = best_model.predict(X_test)

# Save training results to Excel
train_results = pd.DataFrame({'Actual': y_train, 'Predicted': y_train_pred})
train_results.to_excel('Training_Results_Optimized.xlsx', index=False)

# Save testing results to Excel
test_results = pd.DataFrame({'Actual': y_test, 'Predicted': y_test_pred})
test_results.to_excel('Testing_Results_Optimized.xlsx', index=False)

# Save the optimized model
joblib.dump(best_model, 'Optimized_MLP_Model.pkl')

# Find axis limits for consistent scaling
min_value = min(min(y_train), min(y_test), min(y_train_pred), min(y_test_pred))
max_value = max(max(y_train), max(y_test), max(y_train_pred), max(y_test_pred))

# Create scatter plots for the predictions
plt.figure(figsize=(12, 6))

# Actual vs Predicted - Training
plt.subplot(1, 2, 1)
plt.scatter(y_train, y_train_pred, alpha=0.5, color='blue', label='Predicted vs Actual')
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--', linewidth=1.5, label='1:1 Line')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values (Training)')
plt.ylabel('Predicted Values (Training)')
plt.title('Actual vs Predicted - Training Data')
plt.legend()
plt.grid()

# Actual vs Predicted - Testing
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_test_pred, alpha=0.5, color='green', label='Predicted vs Actual')
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--', linewidth=1.5, label='1:1 Line')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values (Testing)')
plt.ylabel('Predicted Values (Testing)')
plt.title('Actual vs Predicted - Testing Data')
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig('Optimized_Scatter_Plots.png')
plt.show()
