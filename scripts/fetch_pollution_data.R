library(httr)
library(jsonlite)
library(dplyr)
library(lubridate)

# API URL
url <- "https://air-quality-api.open-meteo.com/v1/air-quality"
params <- list(
  latitude = 52.52,
  longitude = 13.41,
  hourly = "pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone,ammonia,methane",
  timezone = "Europe/Berlin"
)

# Fetch data from API
response <- GET(url, query = params)
data <- fromJSON(content(response, "text"))

# Convert to DataFrame
df <- as.data.frame(data$hourly)
df$time <- as.POSIXct(df$time, format="%Y-%m-%dT%H:%M:%S")

# Save to CSV
csv_filename <- paste0("data/air_quality_", format(Sys.time(), "%Y-%m-%d_%H-%M-%S"), ".csv")
write.csv(df, csv_filename, row.names = FALSE)

print(paste("Data saved to", csv_filename))
