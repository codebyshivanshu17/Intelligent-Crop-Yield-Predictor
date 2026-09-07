import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import joblib


# Get project folder path
BASE_DIR = Path(__file__).resolve().parent.parent

# Load dataset
DATA_PATH = BASE_DIR / "data" / "crop_yield.csv"

data = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)


# Encode categorical columns
categorical_columns = ["Crop", "Season", "Soil_Type"]

encoders = {}

for column in categorical_columns:
    encoder = LabelEncoder()
    data[column] = encoder.fit_transform(data[column])
    encoders[column] = encoder


# Separate features and target
X = data.drop("Yield", axis=1)
y = data["Yield"]


# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# Train the model
model.fit(X_train, y_train)

print("\nModel trained successfully!")


# Make predictions
predictions = model.predict(X_test)


# Evaluate model
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n----- Model Performance -----")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R2 Score: {r2:.2f}")


# Save the trained model
MODEL_PATH = BASE_DIR / "models" / "crop_yield_model.pkl"

joblib.dump(model, MODEL_PATH)

print("\nModel saved successfully!")
print("Location:", MODEL_PATH)