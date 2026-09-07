import pandas as pd
import joblib
from pathlib import Path


# Get project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load trained model
MODEL_PATH = BASE_DIR / "models" / "crop_yield_model.pkl"

model = joblib.load(MODEL_PATH)


def get_feature_importance():

    # Get feature names
    features = [
        "Crop",
        "Season",
        "Rainfall",
        "Temperature",
        "Humidity",
        "Soil_Type",
        "Nitrogen",
        "Phosphorus",
        "Potassium"
    ]

    # Get importance values from Random Forest
    importance_values = model.feature_importances_

    # Create DataFrame
    importance_data = pd.DataFrame({
        "Feature": features,
        "Importance": importance_values
    })

    # Sort from highest to lowest
    importance_data = importance_data.sort_values(
        by="Importance",
        ascending=False
    )

    return importance_data


# Test the function
if __name__ == "__main__":

    importance_data = get_feature_importance()

    print("\n📊 Feature Importance:\n")
    print(importance_data)