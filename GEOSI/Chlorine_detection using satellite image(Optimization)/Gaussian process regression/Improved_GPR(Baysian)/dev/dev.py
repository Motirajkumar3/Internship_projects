import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
from sklearn.model_selection import train_test_split
from skopt import BayesSearchCV
from skopt.space import Real
import joblib

# Load input and output data
input_file_path = 'Input_X.xlsx'
output_file_path = 'Output_Y.xlsx'

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)

# Prepare data
X = input_data
y = output_data['CHL_a']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define kernel
kernel = C(1.0, (0.01, 10)) * RBF(length_scale=1.0, length_scale_bounds=(0.01, 10))

# Define the model
gp_model = GaussianProcessRegressor(kernel=kernel, random_state=42, normalize_y=True)

# Bayesian Optimization for hyperparameter tuning
param_space = {
    "alpha": Real(1e-6, 1e-2, prior="log-uniform"),  # Noise level
    "kernel__k2__length_scale": Real(0.1, 10, prior="log-uniform"),  # RBF length scale
}

optimizer = BayesSearchCV(
    gp_model,
    search_spaces=param_space,
    n_iter=30,  # Number of optimization iterations
    cv=3,       # 3-fold cross-validation
    n_jobs=-1,  # Use all processors
    random_state=42,
    verbose=0,
)

# Fit the optimized model
optimizer.fit(X_train, y_train)

# Retrieve the best model
best_gp_model = optimizer.best_estimator_

# Predictions for training and testing
y_train_pred = best_gp_model.predict(X_train)
y_test_pred = best_gp_model.predict(X_test)

# Save training results
train_results = pd.DataFrame({'Actual': y_train, 'Predicted': y_train_pred})
train_results.to_excel('Training_Results_Bayesian.xlsx', index=False)

# Save testing results
test_results = pd.DataFrame({'Actual': y_test, 'Predicted': y_test_pred})
test_results.to_excel('Testing_Results_Bayesian.xlsx', index=False)

# Save the best model
joblib.dump(best_gp_model, 'GP_Model_Optimized.pkl')

# Scatterplots with identity line
plt.figure(figsize=(12, 6))

# Find axis limits
min_value = min(y.min(), y_train_pred.min(), y_test_pred.min())
max_value = max(y.max(), y_train_pred.max(), y_test_pred.max())

# Training scatterplot
plt.subplot(1, 2, 1)
plt.scatter(y_train, y_train_pred, alpha=0.5, color='blue', label='Predictions')
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--', label='Identity Line')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual (Training)')
plt.ylabel('Predicted (Training)')
plt.title('Training Data (Optimized)')
plt.legend()
plt.grid()

# Testing scatterplot
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_test_pred, alpha=0.5, color='green', label='Predictions')
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--', label='Identity Line')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual (Testing)')
plt.ylabel('Predicted (Testing)')
plt.title('Testing Data (Optimized)')
plt.legend()
plt.grid()

# Save and show the plot
plt.tight_layout()
plt.savefig('Training_Testing_Scatter_Optimized.png')
plt.show()
