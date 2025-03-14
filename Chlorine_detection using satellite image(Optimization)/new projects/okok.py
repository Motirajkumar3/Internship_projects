import pandas as pd
from sklearn.model_selection import train_test_split
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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=52)

# Initialize and train the Random Forest model
rf_model = RandomForestRegressor(n_estimators=200, random_state=52)
rf_model.fit(X_train, y_train)

# Predict on training and testing datasets
y_train_pred = rf_model.predict(X_train)
y_test_pred = rf_model.predict(X_test)

# Scatter plot for training data
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(y_train, y_train_pred, alpha=0.5, color='blue')
plt.xlabel('Actual Values (Training)')
plt.ylabel('Predicted Values (Training)')
plt.title('Actual vs Predicted - Training Data')
plt.grid()

# Scatter plot for testing data
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_test_pred, alpha=0.5, color='green')
plt.xlabel('Actual Values (Testing)')
plt.ylabel('Predicted Values (Testing)')
plt.title('Actual vs Predicted - Testing Data')
plt.grid()

plt.tight_layout()
plt.show()
