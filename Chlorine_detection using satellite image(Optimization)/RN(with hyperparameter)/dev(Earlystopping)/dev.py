import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

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

# Initialize the Random Forest model
rf_model = RandomForestRegressor(n_estimators=1, random_state=42)

# Initialize variables for early stopping
max_iter = 100
tolerance = 3  # Tolerance to stop when improvement is less than this (after consecutive iterations)
best_score = -float('inf')
no_improvement_count = 0
best_model = None

# Train and monitor the performance incrementally
train_scores = []
for n_estimators in range(1, max_iter + 1):
    rf_model.set_params(n_estimators=n_estimators)
    
    # Perform cross-validation
    cv_score = cross_val_score(rf_model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
    mean_score = cv_score.mean()
    
    # Store the score
    train_scores.append(mean_score)
    
    # Check if the performance has improved
    if mean_score > best_score:
        best_score = mean_score
        best_model = rf_model
        no_improvement_count = 0
    else:
        no_improvement_count += 1
    
    # Early stopping condition: if no improvement for 'tolerance' iterations, stop
    if no_improvement_count >= tolerance:
        print(f"Early stopping after {n_estimators} iterations.")
        break

# Fit the best model to the entire training data
best_model.fit(X_train, y_train)

# Now we can safely make predictions
y_train_pred = best_model.predict(X_train)
y_test_pred = best_model.predict(X_test)

# Save training and testing results to Excel files
train_results = pd.DataFrame({'Actual': y_train, 'Predicted': y_train_pred})
test_results = pd.DataFrame({'Actual': y_test, 'Predicted': y_test_pred})
train_results.to_excel('Training_Results_Early_Stopping.xlsx', index=False)
test_results.to_excel('Testing_Results_Early_Stopping.xlsx', index=False)

# Plot the training performance
plt.plot(range(1, len(train_scores) + 1), train_scores, marker='o', color='blue', label='Train Score')
plt.xlabel('Number of Trees (n_estimators)')
plt.ylabel('Mean CV Score (Negative MSE)')
plt.title('Training Performance Over Iterations')
plt.grid(True)
plt.legend()
plt.show()
