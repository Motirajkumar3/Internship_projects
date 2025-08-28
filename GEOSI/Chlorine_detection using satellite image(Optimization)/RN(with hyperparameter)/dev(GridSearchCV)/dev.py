import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import joblib

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

# Define the base Random Forest model
rf_model = RandomForestRegressor(random_state=42)

# Define hyperparameter space for RandomizedSearchCV
random_param_dist = {
    'n_estimators': [50, 100, 200, 500],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False],
    'max_features': ['auto', 'sqrt', 'log2'],
}

# Perform Randomized Search for broad hyperparameter tuning
random_search = RandomizedSearchCV(estimator=rf_model, param_distributions=random_param_dist, 
                                   n_iter=50, cv=3, random_state=42, n_jobs=-1)
random_search.fit(X_train, y_train)

# Get the best parameters from RandomizedSearchCV
best_random_params = random_search.best_params_
print("Best Parameters from Randomized Search:", best_random_params)

# Use the best parameters from Randomized Search to define a finer GridSearch space
grid_param_dist = {
    'n_estimators': [best_random_params['n_estimators'] - 50, best_random_params['n_estimators'], best_random_params['n_estimators'] + 50],
    'max_depth': [best_random_params['max_depth'] - 5, best_random_params['max_depth'], best_random_params['max_depth'] + 5],
    'min_samples_split': [best_random_params['min_samples_split'], best_random_params['min_samples_split'] + 1],
    'min_samples_leaf': [best_random_params['min_samples_leaf'], best_random_params['min_samples_leaf'] + 1],
    'bootstrap': [best_random_params['bootstrap']],
    'max_features': [best_random_params['max_features']],
}

# Perform Grid Search for finer hyperparameter tuning
grid_search = GridSearchCV(estimator=rf_model, param_grid=grid_param_dist, cv=3, n_jobs=-1)
grid_search.fit(X_train, y_train)

# Get the best parameters from GridSearchCV
best_grid_params = grid_search.best_params_
print("Best Parameters from Grid Search:", best_grid_params)

# Train the final model with the best parameters
final_rf_model = grid_search.best_estimator_

# Predict on training and testing datasets
y_train_pred = final_rf_model.predict(X_train)
y_test_pred = final_rf_model.predict(X_test)

# Save training and testing results to Excel files
train_results = pd.DataFrame({'Actual': y_train, 'Predicted': y_train_pred})
test_results = pd.DataFrame({'Actual': y_test, 'Predicted': y_test_pred})
train_results.to_excel('Training_Results_Tuned.xlsx', index=False)
test_results.to_excel('Testing_Results_Tuned.xlsx', index=False)

# Save the model
joblib.dump(final_rf_model, 'random_forest_model_final.pkl')

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
plt.xlabel('Actual (Testing)')
plt.ylabel('Predicted (Testing)')
plt.title('Testing Data: Actual vs Predicted (Log Scale)')
plt.grid()

# Save the scatter plot
plt.tight_layout()
plt.savefig('Scatter_Plots_Final.png', format='png')
plt.show()

# Evaluate model performance
mae_train = mean_absolute_error(y_train, y_train_pred)
mae_test = mean_absolute_error(y_test, y_test_pred)
print("Mean Absolute Error on Training Data:", mae_train)
print("Mean Absolute Error on Testing Data:", mae_test)
