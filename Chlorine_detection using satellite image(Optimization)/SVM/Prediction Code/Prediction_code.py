import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
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

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the input features using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the Support Vector Machine (SVM) model
svm_model = SVR(kernel='rbf')

# Hyperparameter tuning using GridSearchCV
param_grid = {'C': [1, 10, 100], 'epsilon': [0.1, 0.2, 0.3], 'kernel': ['rbf']}
grid_search = GridSearchCV(svm_model, param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train_scaled, y_train)

# Get the best parameters from GridSearch
svm_model = grid_search.best_estimator_

# Train the model
svm_model.fit(X_train_scaled, y_train)

# Predict on training and testing datasets
y_train_pred = svm_model.predict(X_train_scaled)
y_test_pred = svm_model.predict(X_test_scaled)

# Save training results to Excel
train_results = pd.DataFrame({'Actual': y_train, 'Predicted': y_train_pred})
train_results.to_excel('training_results_svm.xlsx', index=False)

# Save testing results to Excel
test_results = pd.DataFrame({'Actual': y_test, 'Predicted': y_test_pred})
test_results.to_excel('testing_results_svm.xlsx', index=False)

# Save the trained model to a file
joblib.dump(svm_model, 'svm_model.pkl')

# Calculate global axis limits for both training and testing
min_value = min(y_train.min(), y_test.min(), y_train_pred.min(), y_test_pred.min())
max_value = max(y_train.max(), y_test.max(), y_train_pred.max(), y_test_pred.max())

# Plotting the scatter plots for training and testing data
plt.figure(figsize=(12, 6))

# Scatter plot for training data
plt.subplot(1, 2, 1)
plt.scatter(y_train, y_train_pred, alpha=0.5, color='blue')
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
plt.plot(identity_line, identity_line, color='black', label='Identity Line')

# Scatter plot for testing data
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_test_pred, alpha=0.5, color='green')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.xlabel('Actual Values (Testing)')
plt.ylabel('Predicted Values (Testing)')
plt.title('Actual vs Predicted - Testing Data (Log Scale)')
plt.grid()

# Add identity line for testing data
plt.plot(identity_line, identity_line, color='black', label='Identity Line')

# Save the plot as a PNG file
plt.tight_layout()
plt.savefig('svm_scatter_plot_with_identity_line.png')
plt.show()
