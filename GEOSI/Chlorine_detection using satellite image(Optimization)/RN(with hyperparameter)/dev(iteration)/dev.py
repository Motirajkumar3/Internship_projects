import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import joblib

# Load data
input_file_path = 'Input_X.xlsx'  # Replace with your file path
output_file_path = 'Output_Y.xlsx'  # Replace with your file path

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)

# Split data
X = input_data
y = output_data['CHL_a']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Iterative improvement with manual hyperparameter tuning
best_model = None
best_mse = float("inf")

for n_estimators in [100, 200, 300]:  # Number of trees
    for max_depth in [10, 20, 30]:  # Tree depth
        for min_samples_split in [2, 5, 10]:  # Min samples for split
            for min_samples_leaf in [1, 2, 5]:  # Min samples for leaf

                # Train model
                rf_model = RandomForestRegressor(
                    n_estimators=n_estimators,
                    max_depth=max_depth,
                    min_samples_split=min_samples_split,
                    min_samples_leaf=min_samples_leaf,
                    random_state=42,
                )
                rf_model.fit(X_train, y_train)

                # Evaluate on testing data
                y_test_pred = rf_model.predict(X_test)
                mse = mean_squared_error(y_test, y_test_pred)

                print(
                    f"n_estimators={n_estimators}, max_depth={max_depth}, "
                    f"min_samples_split={min_samples_split}, min_samples_leaf={min_samples_leaf}, MSE={mse}"
                )

                # Track best model
                if mse < best_mse:
                    best_mse = mse
                    best_model = rf_model

# Best model results
print("\nBest Model:")
print(f"n_estimators={best_model.n_estimators}, max_depth={best_model.max_depth}, "
      f"min_samples_split={best_model.min_samples_split}, min_samples_leaf={best_model.min_samples_leaf}, MSE={best_mse}")

# Save the best model
joblib.dump(best_model, 'optimized_random_forest_model.pkl')

# Predictions on training and testing datasets
y_train_pred = best_model.predict(X_train)
y_test_pred = best_model.predict(X_test)

# Find axis limits for scatter plots
min_value = min(y_train.min(), y_test.min(), y_train_pred.min(), y_test_pred.min())
max_value = max(y_train.max(), y_test.max(), y_train_pred.max(), y_test_pred.max())

# Create scatter plots
plt.figure(figsize=(12, 6))

# Training scatter plot
plt.subplot(1, 2, 1)
plt.scatter(y_train, y_train_pred, alpha=0.5, color='blue')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--', linewidth=2)  # Diagonal line
plt.xlabel('Actual (Training)')
plt.ylabel('Predicted (Training)')
plt.title('Training Data: Actual vs Predicted (Log Scale)')
plt.grid()

# Testing scatter plot
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_test_pred, alpha=0.5, color='green')
plt.xscale('log')
plt.yscale('log')
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.plot([min_value, max_value], [min_value, max_value], color='red', linestyle='--', linewidth=2)  # Diagonal line
plt.xlabel('Actual (Testing)')
plt.ylabel('Predicted (Testing)')
plt.title('Testing Data: Actual vs Predicted (Log Scale)')
plt.grid()

# Save the scatter plot
plt.tight_layout()
plt.savefig('Improved_Scatter_Plots.png', format='png')
plt.show()

# Save training and testing results to Excel files
train_results = pd.DataFrame({'Actual': y_train, 'Predicted': y_train_pred})
test_results = pd.DataFrame({'Actual': y_test, 'Predicted': y_test_pred})
train_results.to_excel('Improved_Training_Results.xlsx', index=False)
test_results.to_excel('Improved_Testing_Results.xlsx', index=False)
