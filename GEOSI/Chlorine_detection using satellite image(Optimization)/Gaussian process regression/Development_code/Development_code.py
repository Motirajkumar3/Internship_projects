import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C, WhiteKernel
from sklearn.model_selection import train_test_split
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

# Define an optimized Gaussian Process kernel
kernel = C(1.0, (1e-2, 1e2)) * RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e2)) + WhiteKernel(noise_level=1e-2)
gp_model = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10, alpha=1e-6, random_state=42)

# Train the model
gp_model.fit(X_train, y_train)

# Predictions for training and testing
y_train_pred = gp_model.predict(X_train)
y_test_pred = gp_model.predict(X_test)

# Save training results
train_results = pd.DataFrame({'Actual': y_train, 'Predicted': y_train_pred})
train_results.to_excel('Training_Results.xlsx', index=False)

# Save testing results
test_results = pd.DataFrame({'Actual': y_test, 'Predicted': y_test_pred})
test_results.to_excel('Testing_Results.xlsx', index=False)

# Save the model
joblib.dump(gp_model, 'GP_Model_Optimized.pkl')

# Plot scatterplots for training and testing
plt.figure(figsize=(12, 6))

# Determine axis limits for identity line
min_value = min(y.min(), y_train_pred.min(), y_test_pred.min())
max_value = max(y.max(), y_train_pred.max(), y_test_pred.max())

# Scatterplot for training
plt.subplot(1, 2, 1)
plt.scatter(y_train, y_train_pred, alpha=0.5, color='blue', label='Data Points')
plt.plot([min_value, max_value], [min_value, max_value], color='black', label='Identity Line')  # Identity line
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual (Training)')
plt.ylabel('Predicted (Training)')
plt.title('Training Data')
plt.legend()
plt.grid()

# Scatterplot for testing
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_test_pred, alpha=0.5, color='green', label='Data Points')
plt.plot([min_value, max_value], [min_value, max_value], color='black', label='Identity Line')  # Identity line
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual (Testing)')
plt.ylabel('Predicted (Testing)')
plt.title('Testing Data')
plt.legend()
plt.grid()

# Save the plot as PNG
plt.tight_layout()
plt.savefig('Training_Testing_Scatter_Identity_Line.png')
plt.show()
