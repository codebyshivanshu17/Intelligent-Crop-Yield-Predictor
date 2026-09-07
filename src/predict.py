import joblib
import pandas as pd
from pathlib import Path

# Get project folder path
BASE_DIR = Path(__file__).resolve().parent.parent

# Load trained model
MODEL_PATH = BASE_DIR / "models" / "crop_yield_model.pkl"

model = joblib.load(MODEL_PATH)


# IMPORTANT:
# These values must match the encoding used during training

crop_mapping = {
    "Cotton": 0,
    "Maize": 1,
    "Rice": 2,
    "Sugarcane": 3,
    "Wheat": 4
}

season_mapping = {
    "Annual": 0,
    "Kharif": 1,
    "Rabi": 2
}

soil_mapping = {
    "Black": 0,
    "Clay": 1,
    "Loamy": 2,
    "Sandy": 3
}


def predict_crop_yield(
    crop,
    season,
    rainfall,
    temperature,
    humidity,
    soil_type,
    nitrogen,
    phosphorus,
    potassium
):

    # Convert text values into numbers
    crop_encoded = crop_mapping[crop]
    season_encoded = season_mapping[season]
    soil_encoded = soil_mapping[soil_type]

    # Create input data
    input_data = pd.DataFrame(
        [[
            crop_encoded,
            season_encoded,
            rainfall,
            temperature,
            humidity,
            soil_encoded,
            nitrogen,
            phosphorus,
            potassium
        ]],
        columns=[
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
    )

    # Predict yield
    prediction = model.predict(input_data)

    return prediction[0]


# Test prediction
if __name__ == "__main__":

    result = predict_crop_yield(
        crop="Wheat",
        season="Rabi",
        rainfall=700,
        temperature=22,
        humidity=60,
        soil_type="Loamy",
        nitrogen=95,
        phosphorus=45,
        potassium=42
    )

    print("\n🌾 Crop Yield Prediction")
    print(f"Predicted Yield: {result:.2f} Tons/Hectare")