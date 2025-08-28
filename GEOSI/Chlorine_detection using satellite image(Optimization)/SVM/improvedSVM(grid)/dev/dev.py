import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
from skopt import BayesSearchCV
import matplotlib.pyplot as plt
import joblib
import numpy as np

# Load the input and output files
input_file_path = 'Input_X.xlsx'  # Replace with your file path
output_file_path = 'Output_Y.xlsx'  # Replace with your file path

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)

# Split the data into features (X) and target (y)
X = input_data
y = output_data['CHL_a']

# Log-transform the target variable to focus on smaller values
y_log = np.log1p(y)  # log(1 + y) to avoid issues with zero or negative values

# Split the dataset into training and testing sets
X_train, X_test, y_train_log, y_test_log = train_test_split(X, y_log, test_size=0.2, random_state=42)

# Scale the input features using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the Support Vector Machine (SVM) model
svm_model = SVR()

# Define the parameter search space for Bayesian Optimization
param_space = {
    'C': (0.1, 1000.0, 'log-uniform'),
    'epsilon': (0.01, 1.0, 'log-uniform'),
    'gamma': (0.0001, 1.0, 'log-uniform'),
    'kernel': ['rbf']  # Focus on the RBF kernel
}

# Custom scoring function to penalize errors on smaller values
def weighted_mae(y_true, y_pred):
    weights = 1 / (np.expm1(y_true) + 1)  # Higher weight for smaller values (exponential of log-transformed values)
    return np.mean(weights * np.abs(y_true - y_pred))

# Use Bayesian Optimization for hyperparameter tuning
bayes_search = BayesSearchCV(
    estimator=svm_model,
    search_spaces=param_space,
    n_iter=50,  # Number of iterations for optimization
    cv=5,
    scoring='neg_mean_absolute_error',  # Focus on minimizing error
    random_state=42
)

# Fit the model to the training data
bayes_search.fit(X_train_scaled, y_train_log)

# Get the best estimator after tuning
svm_model = bayes_search.best_estimator_

# Train the model with the best parameters
svm_model.fit(X_train_scaled, y_train_log)

# Predict on training and testing datasets
y_train_pred_log = svm_model.predict(X_train_scaled)
y_test_pred_log = svm_model.predict(X_test_scaled)

# Transform predictions back to the original scale
y_train_pred = np.expm1(y_train_pred_log)
y_test_pred = np.expm1(y_test_pred_log)

# Transform actual values back to the original scale
y_train_actual = np.expm1(y_train_log)
y_test_actual = np.expm1(y_test_log)

# Save training results to Excel
train_results = pd.DataFrame({'Actual': y_train_actual, 'Predicted': y_train_pred})
train_results.to_excel('training_results_svm_tuned.xlsx', index=False)

# Save testing results to Excel
test_results = pd.DataFrame({'Actual': y_test_actual, 'Predicted': y_test_pred})
test_results.to_excel('testing_results_svm_tuned.xlsx', index=False)

# Save the trained model to a file
joblib.dump(svm_model, 'svm_model_tuned.pkl')

# Calculate global axis limits for both training and testing
min_value = min(y_train_actual.min(), y_test_actual.min(), y_train_pred.min(), y_test_pred.min())
max_value = max(y_train_actual.max(), y_test_actual.max(), y_train_pred.max(), y_test_pred.max())

# Plotting the scatter plots for training and testing data
plt.figure(figsize=(12, 6))

# Scatter plot for training data
plt.subplot(1, 2, 1)
plt.scatter(y_train_actual, y_train_pred, alpha=0.5, color='blue')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values (Training)')
plt.ylabel('Predicted Values (Training)')
plt.title('Actual vs Predicted - Training Data (Log Scale)')
plt.grid()

# Add identity line for training data
identity_line = np.linspace(min_value, max_value, 100)
plt.plot(identity_line, identity_line, color='red', linestyle='--', label='Identity Line')

# Scatter plot for testing data
plt.subplot(1, 2, 2)
plt.scatter(y_test_actual, y_test_pred, alpha=0.5, color='green')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values (Testing)')
plt.ylabel('Predicted Values (Testing)')
plt.title('Actual vs Predicted - Testing Data (Log Scale)')
plt.grid()

# Add identity line for testing data
plt.plot(identity_line, identity_line, color='red', linestyle='--', label='Identity Line')

# Save the plot as a PNG file
plt.tight_layout()
plt.savefig('svm_scatter_plot_with_identity_line_tuned.png')
plt.show()
