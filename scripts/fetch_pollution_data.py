import requests
import pandas as pd
from datetime import datetime

# API URL
API_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"
PARAMS = {
    "latitude": 52.52,  # Berlin as an example
    "longitude": 13.41,
    "hourly": "pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone,ammonia,methane",
    "timezone": "Europe/Berlin"
}

# Fetch data from API
response = requests.get(API_URL, params=PARAMS)
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data["hourly"])
df["time"] = pd.to_datetime(df["time"])

# Save to CSV
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
csv_filename = f"data/air_quality_{timestamp}.csv"
df.to_csv(csv_filename, index=False)

print(f"Data saved to {csv_filename}")
