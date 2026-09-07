import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv("data/crop_yield.csv")

print("\nOriginal Dataset:")
print(data.head())

# Create LabelEncoder
label_encoder = LabelEncoder()

# Columns that contain text
categorical_columns = ["Crop", "Season", "Soil_Type"]

# Convert text data into numbers
for column in categorical_columns:
    data[column] = label_encoder.fit_transform(data[column])

print("\nDataset After Encoding:")
print(data.head())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Separate input features and target
X = data.drop("Yield", axis=1)
y = data["Yield"]

print("\nInput Features (X):")
print(X.head())

print("\nTarget Variable (y):")
print(y.head())

print("\nData Preprocessing Completed Successfully!")