# -*- coding: utf-8 -*-
"""Copy of randomforestregressor.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t9HjiyeaXggVN3BxNVy7E3Trm_qAwmH8
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

input_data = pd.read_excel('Input_X.xlsx')
output_data = pd.read_excel('Output_Y.xlsx')

input_data.head()

output_data.head()

# Checking for missing values in input and output data
print("Missing values in input data:")
print(input_data.isnull().sum())

print("\nMissing values in output data:")
print(output_data.isnull().sum())

# Replace zeros with NaN to treat them as missing values
input_data.replace(0, np.nan, inplace=True)

# Drop rows with any NaN values (this will drop rows with original NaNs or replaced zeros)
input_data.dropna(inplace=True)

# Reset the index after dropping rows
input_data.reset_index(drop=True, inplace=True)

X = input_data
y = output_data['CHL_a']

y = y.values.ravel()  # Flatten to 1D array, as required by the model

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Feature Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print(y.shape)  # Check the shape of the target variable

print(X.shape)

y = y.ravel()  # Convert y to shape (n_samples,)

print(f"Train shapes: X_train = {X_train.shape}, y_train = {y_train.shape}")
print(f"Test shapes: X_test = {X_test.shape}, y_test = {y_test.shape}")

def check_shapes(X, y):
    assert len(X) == len(y), "Mismatch: X and y must have the same number of samples."
    print(f"Shapes are aligned: X = {X.shape}, y = {y.shape}")

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

# Generate synthetic dataset with realistic variability
np.random.seed(42)
X = np.random.rand(2000, 5) * 100  # Larger variability
y = (X[:, 0] * 1.5 + X[:, 1] * 2 + np.random.rand(2000) * 50)  # Non-linear relationship

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hyperparameter tuning for Random Forest
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 15, 20],
    'min_samples_split': [2, 5, 10]
}

rf_model = GridSearchCV(
    RandomForestRegressor(random_state=42),
    param_grid=param_grid,
    cv=3,
    scoring='neg_mean_squared_error',
    verbose=1
)

# Train model with optimal hyperparameters
rf_model.fit(X_train, y_train)
best_params = rf_model.best_params_
print("Best Parameters:", best_params)

# Predict on train and test data
y_train_pred = rf_model.predict(X_train)
y_test_pred = rf_model.predict(X_test)

# Evaluate performance
mse_train = mean_squared_error(y_train, y_train_pred)
r2_train = r2_score(y_train, y_train_pred)

mse_test = mean_squared_error(y_test, y_test_pred)
r2_test = r2_score(y_test, y_test_pred)

print(f"Training MSE: {mse_train:.2f}, R2: {r2_train:.2f}")
print(f"Testing MSE: {mse_test:.2f}, R2: {r2_test:.2f}")

# Plot true vs predicted for both train and test
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Training scatter plot
axs[0].scatter(y_train, y_train_pred, alpha=0.5, color="blue", label="Train Data")
axs[0].plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2, label="Ideal Fit")
axs[0].set_xlabel("True Values (Train)")
axs[0].set_ylabel("Predicted Values (Train)")
axs[0].set_xscale('log')
axs[0].set_yscale('log')
axs[0].set_xlim(10**2,10**3)
axs[0].set_ylim(10**2,10**3)
axs[0].set_title("Random Forest - Training: True vs Predicted")
axs[0].legend()
axs[0].grid(True)

# Testing scatter plot
axs[1].scatter(y_test, y_test_pred, alpha=0.5, color="orange", label="Test Data")
axs[1].plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2, label="Ideal Fit")
axs[1].set_xlabel("True Values (Test)")
axs[1].set_ylabel("Predicted Values (Test)")
axs[1].set_xscale('log')
axs[1].set_yscale('log')
axs[1].set_xlim(10**2,10**3)
axs[1].set_ylim(10**2,10**3)
axs[1].set_title("Random Forest - Testing: True vs Predicted")
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

# Synthetic data generation (replace with your actual dataset)
np.random.seed(42)
X = np.random.rand(1000, 5)  # 1000 samples, 5 features
y = np.random.rand(1000)     # Target variable

# Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Regressor (without hyperparameter tuning)
rf_model = RandomForestRegressor(
    n_estimators=200,  # Increased trees for stability
    max_depth=10,      # Controlled depth to prevent overfitting
    random_state=42
)

# Train the model
rf_model.fit(X_train, y_train)

# Predict on training and testing sets
y_train_pred = rf_model.predict(X_train)
y_test_pred = rf_model.predict(X_test)

# Evaluate model performance
mse_train = mean_squared_error(y_train, y_train_pred)
rmse_train = np.sqrt(mse_train)
r2_train = r2_score(y_train, y_train_pred)

mse_test = mean_squared_error(y_test, y_test_pred)
rmse_test = np.sqrt(mse_test)
r2_test = r2_score(y_test, y_test_pred)

print(f"Training - MSE: {mse_train:.4f}, RMSE: {rmse_train:.4f}, R2: {r2_train:.4f}")
print(f"Testing - MSE: {mse_test:.4f}, RMSE: {rmse_test:.4f}, R2: {r2_test:.4f}")

# Plot true vs predicted values for training and testing sets
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Training scatter plot
axs[0].scatter(y_train, y_train_pred, alpha=0.5, color="blue")
axs[0].plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()], 'r--', lw=2)
axs[0].set_xlabel("True Values (Train)")
axs[0].set_ylabel("Predicted Values (Train)")
axs[0].set_title("Random Forest Regression - Training")
axs[0].grid(True)

# Testing scatter plot
axs[1].scatter(y_test, y_test_pred, alpha=0.5, color="orange")
axs[1].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
axs[1].set_xlabel("True Values (Test)")
axs[1].set_ylabel("Predicted Values (Test)")
axs[1].set_title("Random Forest Regression - Testing")
axs[1].grid(True)

plt.tight_layout()
plt.show()

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

# Synthetic data generation (replace with your actual dataset)
np.random.seed(42)
X = np.random.rand(1000, 5)  # 1000 samples, 5 features
y = np.random.rand(1000)     # Target variable

# Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Regressor (without hyperparameter tuning)
rf_model = RandomForestRegressor(
    n_estimators=200,  # Increased trees for stability
    max_depth=10,      # Controlled depth to prevent overfitting
    random_state=42
)

# Train the model
rf_model.fit(X_train, y_train)

# Predict on training and testing sets
y_train_pred = rf_model.predict(X_train)
y_test_pred = rf_model.predict(X_test)

# Evaluate model performance
mse_train = mean_squared_error(y_train, y_train_pred)
rmse_train = np.sqrt(mse_train)
r2_train = r2_score(y_train, y_train_pred)

mse_test = mean_squared_error(y_test, y_test_pred)
rmse_test = np.sqrt(mse_test)
r2_test = r2_score(y_test, y_test_pred)

print(f"Training - MSE: {mse_train:.4f}, RMSE: {rmse_train:.4f}, R2: {r2_train:.4f}")
print(f"Testing - MSE: {mse_test:.4f}, RMSE: {rmse_test:.4f}, R2: {r2_test:.4f}")

# Plot true vs predicted values for training and testing sets
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Training scatter plot
axs[0].scatter(y_train, y_train_pred, alpha=0.5, color="blue")
axs[0].plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()], 'r--', lw=2)
axs[0].set_xlabel("True Values (Train)")
axs[0].set_ylabel("Predicted Values (Train)")
axs[0].set_xscale('log')
axs[0].set_yscale('log')
axs[0].set_xlim(10**-2, 10**4)  # Adjust as per your data range
axs[0].set_ylim(10**-2, 10**4)
axs[0].set_title("Random Forest Regression - Training")
axs[0].grid(True)

# Testing scatter plot
axs[1].scatter(y_test, y_test_pred, alpha=0.5, color="orange")
axs[1].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
axs[1].set_xlabel("True Values (Test)")
axs[1].set_ylabel("Predicted Values (Test)")
axs[1].set_xscale('log')
axs[1].set_yscale('log')
axs[1].set_xlim(10**-2, 10**4)  # Adjust as per your data range
axs[1].set_ylim(10**-2, 10**4)
axs[1].set_title("Random Forest Regression - Testing")
axs[1].grid(True)

plt.tight_layout()
plt.show()