import json
import random
import os
from datetime import datetime

FILE_NAME = "weather.json"

def get_weather():
    # 1. Load previous data to ensure continuity
    try:
        with open(FILE_NAME, 'r') as f:
            old_data = json.load(f)
            last_temp = old_data.get("temp_c", 12.0)
    except:
        last_temp = 12.0

    # 2. Intelligent Drift (Realistic for ÖestVèl/Harrogate)
    # Temp won't jump more than 1.2 degrees per hour
    drift = random.uniform(-1.2, 1.2)
    new_temp = round(last_temp + drift, 1)
    
    # Keep it within realistic bounds for the region
    new_temp = max(min(new_temp, 28), -4)

    # 3. Logic for conditions
    if new_temp < 2: cond = "Freezing/Misty"
    elif new_temp < 12: cond = "Overcast"
    elif new_temp < 20: cond = "Partly Cloudy"
    else: cond = "Clear Skies"

    # 4. Generate the payload
    weather_update = {
        "location": "ÖestVèl Centrè",
        "temp_c": new_temp,
        "condition": cond,
        "wind_kmh": random.randint(5, 20),
        "energy_tax": f"VC€ {round(abs(18 - new_temp) * 0.35, 2)}",
        "last_updated": datetime.now().strftime("%H:%M OVST"),
        "ref_code": "AS-20260203-0834"
    }

    with open(FILE_NAME, 'w') as f:
        json.dump(weather_update, f, indent=4)

if __name__ == "__main__":
    get_weather()
