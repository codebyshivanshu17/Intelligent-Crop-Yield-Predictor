import streamlit as st
import sys
from pathlib import Path
import pandas as pd
import plotly.express as px

# Get project directory
BASE_DIR = Path(__file__).resolve().parent

# Load dataset
DATA_PATH = BASE_DIR / "data" / "crop_yield.csv"

data = pd.read_csv(DATA_PATH)

# Add src folder to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR / "src"))

from predict import predict_crop_yield
from weather_analysis import analyze_weather
from feature_importance import get_feature_importance


# Page configuration
st.set_page_config(
    page_title="AgriTech AI",
    page_icon="🌾",
    layout="wide"
)
# Sidebar
st.sidebar.title("🌾 AgriTech AI")

st.sidebar.write("### Intelligent Agriculture System")
st.sidebar.divider()

page = st.sidebar.radio(
    "🧭 Navigation",
    [
        "🏠 Home",
        "🌾 Crop Prediction",
        "🌦️ Weather Analysis",
        "📊 Analytics",
        "🤖 AI Insights"
    ]
)
# ==============================
# HOME PAGE
# ==============================
if page == "🏠 Home":
    st.title("🌾 Intelligent Crop Yield Predictor")
    st.subheader("🤖 AI-Powered Agriculture Decision Support System")
    st.write(
        "Predict crop yield using Machine Learning and analyze "
        "weather conditions to support smarter agricultural decisions."
    )

    st.divider()

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric(label="🌾 Supported Crops", value="5")

    with metric2:
        st.metric(label="🤖 ML Model", value="Random Forest")

    with metric3:
        st.metric(label="📊 Dataset Records", value=len(data))

    st.divider()

    st.subheader("🚀 What Can This System Do?")
    st.write("🌾 Predict crop yield using Machine Learning")
    st.write("🌦️ Analyze crop-specific weather conditions")
    st.write("🤖 Provide smart farming recommendations")
    st.write("📊 Display agricultural analytics")
    st.write("🔍 Explain AI model feature importance")

    st.divider()

    st.header("🤖 AI Model Feature Importance")

    importance_data = get_feature_importance().sort_values(
        by="Importance",
        ascending=True
    )

    fig_importance = px.bar(
        importance_data,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Factors Affecting Crop Yield"
    )

    st.plotly_chart(fig_importance, use_container_width=True)

# ==============================
# CROP PREDICTION PAGE
# ==============================
elif page == "🌾 Crop Prediction":
    st.title("🌾 Crop Yield Prediction")
    st.write(
        "Enter crop, weather, and soil information to predict the expected crop yield."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌱 Crop Information")

        crop = st.selectbox(
            "Select Crop",
            ["Wheat", "Rice", "Maize", "Sugarcane", "Cotton"]
        )

        season = st.selectbox(
            "Select Season",
            ["Rabi", "Kharif", "Annual"]
        )

        soil_type = st.selectbox(
            "Select Soil Type",
            ["Loamy", "Clay", "Sandy", "Black"]
        )

        rainfall = st.number_input(
            "Rainfall (mm)",
            min_value=0.0,
            value=700.0
        )

    with col2:
        st.subheader("🌦️ Weather & Soil Conditions")

        temperature = st.number_input(
            "Temperature (°C)",
            min_value=0.0,
            value=25.0
        )

        humidity = st.number_input(
            "Humidity (%)",
            min_value=0.0,
            max_value=100.0,
            value=60.0
        )

        nitrogen = st.number_input(
            "Nitrogen Level",
            min_value=0.0,
            value=90.0
        )

        phosphorus = st.number_input(
            "Phosphorus Level",
            min_value=0.0,
            value=45.0
        )

        potassium = st.number_input(
            "Potassium Level",
            min_value=0.0,
            value=40.0
        )

    st.divider()

    if st.button("🚀 Analyze & Predict Crop Yield", use_container_width=True):
        prediction = predict_crop_yield(
            crop,
            season,
            rainfall,
            temperature,
            humidity,
            soil_type,
            nitrogen,
            phosphorus,
            potassium
        )

        weather_score, weather_status, recommendations = analyze_weather(
            crop,
            rainfall,
            temperature,
            humidity
        )

        st.success("Analysis Completed Successfully! 🎉")

        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.metric(
                label="🌾 Predicted Crop Yield",
                value=f"{prediction:.2f} Tons/Hectare"
            )

        with result_col2:
            st.metric(
                label="🌦️ Weather Suitability Score",
                value=f"{weather_score}/100"
            )

        st.subheader("🌦️ Weather Impact Analysis")
        st.write(weather_status)

        st.subheader("🤖 Smart Farming Recommendations")

        for recommendation in recommendations:
            st.write(recommendation)

# ==============================
# WEATHER ANALYSIS PAGE
# ==============================
elif page == "🌦️ Weather Analysis":
    st.title("🌦️ Crop-Specific Weather Analysis")
    st.write(
        "Analyze whether current weather conditions are suitable for a selected crop."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌱 Select Crop")

        weather_crop = st.selectbox(
            "Select Crop",
            ["Wheat", "Rice", "Maize", "Sugarcane", "Cotton"],
            key="weather_crop"
        )

        weather_rainfall = st.number_input(
            "Rainfall (mm)",
            min_value=0.0,
            value=700.0,
            key="weather_rainfall"
        )

    with col2:
        st.subheader("🌦️ Weather Conditions")

        weather_temperature = st.number_input(
            "Temperature (°C)",
            min_value=0.0,
            value=25.0,
            key="weather_temperature"
        )

        weather_humidity = st.number_input(
            "Humidity (%)",
            min_value=0.0,
            max_value=100.0,
            value=60.0,
            key="weather_humidity"
        )

    st.divider()

    if st.button("🌦️ Analyze Weather Conditions", use_container_width=True):
        weather_score, weather_status, recommendations = analyze_weather(
            weather_crop,
            weather_rainfall,
            weather_temperature,
            weather_humidity
        )

        st.success("Weather Analysis Completed Successfully! 🎉")

        metric_col1, metric_col2 = st.columns(2)

        with metric_col1:
            st.metric("🌦️ Weather Suitability Score", f"{weather_score}/100")

        with metric_col2:
            st.metric("🌱 Selected Crop", weather_crop)

        st.divider()

        st.subheader("📊 Weather Status")
        st.write(weather_status)

        st.subheader("🤖 Smart Farming Recommendations")

        for recommendation in recommendations:
            st.write(recommendation)

# ==============================
# ANALYTICS PAGE
# ==============================
# ==============================
# ANALYTICS PAGE
# ==============================

elif page == "📊 Analytics":

    st.title("📊 Agricultural Data Analytics")

    st.write(
        "Explore crop yield patterns and relationships between weather conditions and crop production."
    )

    st.divider()

    # Create two columns for charts
    chart_col1, chart_col2 = st.columns(2)

    # 🌧️ Rainfall vs Yield
    with chart_col1:

        fig_rainfall = px.scatter(
            data,
            x="Rainfall",
            y="Yield",
            color="Crop",
            title="🌧️ Rainfall vs Crop Yield",
            size="Yield",
            hover_data=["Season", "Soil_Type"]
        )

        st.plotly_chart(
            fig_rainfall,
            use_container_width=True
        )

    # 🌡️ Temperature vs Yield
    with chart_col2:

        fig_temperature = px.scatter(
            data,
            x="Temperature",
            y="Yield",
            color="Crop",
            title="🌡️ Temperature vs Crop Yield",
            size="Yield",
            hover_data=["Season", "Soil_Type"]
        )

        st.plotly_chart(
            fig_temperature,
            use_container_width=True
        )

    st.divider()

    # 🌾 Average Yield by Crop
    st.subheader("🌾 Average Crop Yield")

    average_yield = (
        data.groupby("Crop")["Yield"]
        .mean()
        .reset_index()
    )

    fig_average_yield = px.bar(
        average_yield,
        x="Crop",
        y="Yield",
        color="Crop",
        title="🌾 Average Yield by Crop"
    )

    st.plotly_chart(
        fig_average_yield,
        use_container_width=True
    )

    # Dataset Preview
    st.divider()

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        data,
        use_container_width=True
    )
# ==============================
# AI INSIGHTS PAGE
# ==============================
elif page == "🤖 AI Insights":
    st.title("🤖 AI Insights")
    st.subheader("Smart recommendations from the crop intelligence system")

    st.write(
        "This page highlights the model's feature importance and the main drivers "
        "of crop productivity."
    )

    st.divider()

    importance_data = get_feature_importance().sort_values(by="Importance", ascending=True)

    fig_importance = px.bar(
        importance_data,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Factors Affecting Crop Yield"
    )

    st.plotly_chart(fig_importance, use_container_width=True)

    st.subheader("💡 Recommendations")
    st.write("- Focus on rainfall and temperature balance for crop health.")
    st.write("- Maintain soil nutrients to improve yield stability.")
    st.write("- Use local weather and rainfall data for seasonal planning.")

else:
    st.title("🌾 Intelligent Crop Yield Predictor")
    st.subheader("🤖 AI-Powered Agriculture Decision Support System")
    st.write(
        "Predict crop yield using Machine Learning and analyze weather conditions to "
        "support smarter agricultural decisions."
    )

st.sidebar.info(
    """
    This AI-powered application helps predict crop yield
    and analyze weather conditions.
    """
)

st.sidebar.write("### Features")
st.sidebar.write("🌾 Crop Yield Prediction")
st.sidebar.write("🌦️ Weather Analysis")
st.sidebar.write("📊 Agricultural Analytics")
st.sidebar.write("🤖 Smart Recommendations")
st.sidebar.caption("Developed using Python, Machine Learning & Streamlit")