import pandas as pd
import matplotlib.pyplot as plt

# Load Data
csv_file = "data/air_quality_latest.csv"

try:
    df = pd.read_csv(csv_file)

    # Convert 'time' column to datetime format
    df["time"] = pd.to_datetime(df["time"])

    # Plot Data
    plt.figure(figsize=(12, 6))
    plt.plot(df["time"], df["pm2_5"], label="PM2.5", color="red", linestyle="--")
    plt.plot(df["time"], df["pm10"], label="PM10", color="blue", linestyle="-")

    plt.xlabel("Time")
    plt.ylabel("Pollutant Levels (µg/m³)")
    plt.title("PM2.5 & PM10 Levels Over Time")
    plt.legend()
    plt.grid(True)

    # Rotate x-axis labels for readability
    plt.xticks(rotation=45)

    # Save Plot for Quarto
    plot_path = "docs/pm_pollution_trend.png"
    plt.savefig(plot_path, bbox_inches="tight")
    plt.show()

    print(f"✅ Plot saved to {plot_path}")

except FileNotFoundError:
    print(f"❌ Error: {csv_file} not found. Run the data fetching script first.")
