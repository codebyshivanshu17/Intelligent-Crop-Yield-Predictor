def analyze_weather(crop, rainfall, temperature, humidity):

    # Ideal conditions for each crop
    crop_conditions = {
        "Wheat": {
            "rainfall": (500, 900),
            "temperature": (15, 25),
            "humidity": (40, 70)
        },

        "Rice": {
            "rainfall": (1000, 1600),
            "temperature": (20, 35),
            "humidity": (70, 90)
        },

        "Maize": {
            "rainfall": (600, 1000),
            "temperature": (20, 30),
            "humidity": (50, 75)
        },

        "Sugarcane": {
            "rainfall": (900, 1500),
            "temperature": (25, 35),
            "humidity": (60, 85)
        },

        "Cotton": {
            "rainfall": (500, 900),
            "temperature": (25, 35),
            "humidity": (45, 70)
        }
    }

    conditions = crop_conditions[crop]

    score = 100
    recommendations = []

    # Rainfall analysis
    min_rain, max_rain = conditions["rainfall"]

    if rainfall < min_rain:
        score -= 25
        recommendations.append(
            f"⚠️ Rainfall is lower than the ideal range for {crop}. Consider irrigation."
        )

    elif rainfall > max_rain:
        score -= 20
        recommendations.append(
            f"⚠️ Rainfall is higher than the ideal range for {crop}. Ensure proper drainage."
        )

    else:
        recommendations.append(
            f"✅ Rainfall is suitable for {crop}."
        )

    # Temperature analysis
    min_temp, max_temp = conditions["temperature"]

    if temperature < min_temp:
        score -= 20
        recommendations.append(
            f"⚠️ Temperature is lower than the ideal range for {crop}."
        )

    elif temperature > max_temp:
        score -= 20
        recommendations.append(
            f"⚠️ Temperature is higher than the ideal range for {crop}."
        )

    else:
        recommendations.append(
            f"✅ Temperature is suitable for {crop}."
        )

    # Humidity analysis
    min_humidity, max_humidity = conditions["humidity"]

    if humidity < min_humidity:
        score -= 15
        recommendations.append(
            f"⚠️ Humidity is lower than the ideal range for {crop}."
        )

    elif humidity > max_humidity:
        score -= 15
        recommendations.append(
            f"⚠️ Humidity is higher than the ideal range for {crop}."
        )

    else:
        recommendations.append(
            f"✅ Humidity is suitable for {crop}."
        )

    # Keep score between 0 and 100
    score = max(0, min(100, score))

    # Final status
    if score >= 80:
        status = "🟢 Favorable Weather"
    elif score >= 50:
        status = "🟡 Moderate Weather Risk"
    else:
        status = "🔴 Unfavorable Weather"

    return score, status, recommendations