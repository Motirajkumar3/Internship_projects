import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
import joblib
import numpy as np

# Load the data
input_file_path = 'Input_X.xlsx'  # Replace with your file path
output_file_path = 'Output_Y.xlsx'  # Replace with your file path

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)

# Split data
X = input_data
y = output_data['CHL_a']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the MLP model
mlp_model = MLPRegressor(max_iter=1000, random_state=42)

# Define reduced hyperparameter space
param_space = {
    'hidden_layer_sizes': [(50,), (100,), (50, 50)],
    'alpha': [1e-4, 1e-3, 1e-2],  # Reduced options for regularization
    'learning_rate_init': [1e-4, 1e-3],  # Fewer learning rate values
    'solver': ['adam'],  # Fixed solver for simplicity
    'activation': ['relu'],  # Single activation function
}

# Perform Randomized Search
opt = RandomizedSearchCV(
    estimator=mlp_model,
    param_distributions=param_space,
    n_iter=10,  # Reduced iterations
    cv=3,  # 3-fold cross-validation
    scoring='neg_mean_squared_error',
    random_state=42,
    verbose=0,
)

# Fit the optimized model
opt.fit(X_train, y_train)
best_model = opt.best_estimator_

# Save the best model
joblib.dump(best_model, 'Optimized_MLP_Model_Fast.pkl')

# Predictions
y_train_pred = best_model.predict(X_train)
y_test_pred = best_model.predict(X_test)

# Save training results to Excel
train_results = pd.DataFrame({'Actual': y_train, 'Predicted': y_train_pred})
train_results.to_excel('Training_Results_Fast.xlsx', index=False)

# Save testing results to Excel
test_results = pd.DataFrame({'Actual': y_test, 'Predicted': y_test_pred})
test_results.to_excel('Testing_Results_Fast.xlsx', index=False)

# Find axis limits for consistent scaling
min_value = min(min(y_train), min(y_test), min(y_train_pred), min(y_test_pred))
max_value = max(max(y_train), max(y_test), max(y_train_pred), max(y_test_pred))

# Create scatter plots for training and testing predictions
plt.figure(figsize=(12, 6))

# Training scatter plot
plt.subplot(1, 2, 1)
plt.scatter(y_train, y_train_pred, alpha=0.5, color='blue', label='Predicted vs Actual')
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--', linewidth=1.5, label='1:1 Line')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values (Training)')
plt.ylabel('Predicted Values (Training)')
plt.title('Training Data: Actual vs Predicted')
plt.legend()
plt.grid()

# Testing scatter plot
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_test_pred, alpha=0.5, color='green', label='Predicted vs Actual')
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--', linewidth=1.5, label='1:1 Line')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values (Testing)')
plt.ylabel('Predicted Values (Testing)')
plt.title('Testing Data: Actual vs Predicted')
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig('Scatter_Plot_Training_Testing_Fast.png')
plt.show()
