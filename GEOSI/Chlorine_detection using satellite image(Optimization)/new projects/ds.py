import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load the input and output files
input_file_path = 'Input_X.xlsx'  # Replace with your file path
output_file_path = 'Output_Y.xlsx'  # Replace with your file path

input_data = pd.read_excel(input_file_path)
output_data = pd.read_excel(output_file_path)

# Split the data into features (X) and target (y)
X = input_data
y = output_data['CHL_a']

# Train the Random Forest model on the entire dataset
rf_model = RandomForestRegressor(n_estimators=200, random_state=52)
rf_model.fit(X, y)

# Example manual input for testing (replace with your own values)
manual_input = [[0.003998,0.003865,0.004595,0.005194,0.010416,0.0159,0.017555,0.007639,0.005075,0.0049680,0.000711]]

# Predict the output for the manual input
predicted_output = rf_model.predict(manual_input)

print("Predicted Output:", predicted_output)
