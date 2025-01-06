import requests
import matplotlib.pyplot as plt
import pandas as pd


CITY = 'Kolkata'
LATITUDE = 22.5726
LONGITUDE = 88.3639


URL = f'https://api.open-meteo.com/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Asia%2FKolkata'

# Fetching data from the API
response = requests.get(URL)
data = response.json()

# Extracting relevant data
dates = data['daily']['time']
temp_max = data['daily']['temperature_2m_max']
temp_min = data['daily']['temperature_2m_min']
precipitation = data['daily']['precipitation_sum']

# Creating a DataFrame
weather_df = pd.DataFrame({
    'Date': pd.to_datetime(dates),
    'Temp_Max (°C)': temp_max,
    'Temp_Min (°C)': temp_min,
    'Precipitation (mm)': precipitation
})

# Plotting Temperature over Time
plt.figure(figsize=(12, 6))
plt.plot(weather_df['Date'], weather_df['Temp_Max (°C)'], label='Max Temperature (°C)', color='red', marker='o')
plt.plot(weather_df['Date'], weather_df['Temp_Min (°C)'], label='Min Temperature (°C)', color='blue', marker='o')
plt.fill_between(weather_df['Date'], weather_df['Temp_Min (°C)'], weather_df['Temp_Max (°C)'], color='lightgray', alpha=0.5)
plt.title(f'7-Day Weather Forecast for {CITY}')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plotting Precipitation over Time
plt.figure(figsize=(12, 6))
plt.bar(weather_df['Date'], weather_df['Precipitation (mm)'], color='blue', alpha=0.7)
plt.title(f'7-Day Precipitation Forecast for {CITY}')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.ylabel('Precipitation (mm)')
plt.grid(True)
plt.tight_layout()
plt.show()