import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("data/air_quality_latest.csv")

# Plot Data
plt.figure(figsize=(10,5))
plt.plot(df["time"], df["pm2_5"], label="PM2.5", color="red")
plt.plot(df["time"], df["pm10"], label="PM10", color="blue")

plt.xlabel("Time")
plt.ylabel("Pollutant Levels")
plt.title("PM2.5 & PM10 Levels Over Time")
plt.legend()
plt.show()
