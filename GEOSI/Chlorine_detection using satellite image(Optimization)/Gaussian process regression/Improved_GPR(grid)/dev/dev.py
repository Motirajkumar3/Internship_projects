import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C, WhiteKernel
from sklearn.model_selection import train_test_split, GridSearchCV
import joblib

# Load input and output data
input_file_path = 'Input_X.xlsx'
output_file_path = 'Output_Y.xlsx'

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)

# Prepare data
X = input_data
y = output_data['CHL_a']

# Apply logarithmic transformation to the target variable
y_log = np.log1p(y)  # log(1 + y) to handle zero values

# Split data into training and testing sets (80:20 ratio)
X_train, X_test, y_train, y_test = train_test_split(X, y_log, test_size=0.2, random_state=42)

# Define a more flexible kernel with noise modeling
kernel = C(1.0, (1e-2, 1e3)) * RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e3)) + WhiteKernel(noise_level=1e-5)

# Initialize Gaussian Process Regressor
gp = GaussianProcessRegressor()

# Define hyperparameter grid for grid search
param_grid = {
    "alpha": [1e-10, 1e-5, 1e-3],  # Noise level
    "kernel": [
        C(1.0, (1e-2, 1e3)) * RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e3)) + WhiteKernel(noise_level=1e-5),
        C(10.0, (1e-2, 1e3)) * RBF(length_scale=0.5, length_scale_bounds=(1e-2, 1e3)) + WhiteKernel(noise_level=1e-5),
    ],
    "n_restarts_optimizer": [0, 5],
}

# Perform grid search to find the best hyperparameters
grid_search = GridSearchCV(estimator=gp, param_grid=param_grid, cv=3, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Get the best model
best_gp_model = grid_search.best_estimator_

# Save the model
joblib.dump(best_gp_model, 'Improved_GP_Model_Log_Transformed.pkl')

# Predictions for training and testing
y_train_pred_log = best_gp_model.predict(X_train)
y_test_pred_log = best_gp_model.predict(X_test)

# Revert predictions back to original scale using exponential transformation
y_train_pred = np.expm1(y_train_pred_log)  # exp(y) - 1
y_test_pred = np.expm1(y_test_pred_log)
y_train_actual = np.expm1(y_train)
y_test_actual = np.expm1(y_test)

# Save training results
train_results = pd.DataFrame({'Actual': y_train_actual, 'Predicted': y_train_pred})
train_results.to_excel('Improved_Training_Results_Log_Transformed.xlsx', index=False)

# Save testing results
test_results = pd.DataFrame({'Actual': y_test_actual, 'Predicted': y_test_pred})
test_results.to_excel('Improved_Testing_Results_Log_Transformed.xlsx', index=False)

# Scatterplots with identity line
plt.figure(figsize=(12, 6))

# Find axis limits
min_value = min(y.min(), y_train_pred.min(), y_test_pred.min())
max_value = max(y.max(), y_train_pred.max(), y_test_pred.max())

# Training scatterplot
plt.subplot(1, 2, 1)
plt.scatter(y_train_actual, y_train_pred, alpha=0.5, color='blue', label='Predictions')
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--', label='Identity Line')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual (Training)')
plt.ylabel('Predicted (Training)')
plt.title('Training Data (Log-Transformed)')
plt.legend()
plt.grid()

# Testing scatterplot
plt.subplot(1, 2, 2)
plt.scatter(y_test_actual, y_test_pred, alpha=0.5, color='green', label='Predictions')
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--', label='Identity Line')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual (Testing)')
plt.ylabel('Predicted (Testing)')
plt.title('Testing Data (Log-Transformed)')
plt.legend()
plt.grid()

# Save and show the plot
plt.tight_layout()
plt.savefig('Improved_Training_Testing_Scatter_Log_Transformed.png')
plt.show()
