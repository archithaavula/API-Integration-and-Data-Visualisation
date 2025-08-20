import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Config
API_KEY = 'your_api_key_here'  # Replace with your actual key
CITY = 'Chennai'
UNITS = 'metric'  # 'imperial' for Fahrenheit

# API Request
url = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}'
response = requests.get(url)
data = response.json()

# Check response
if response.status_code != 200:
    print("Error fetching data:", data.get("message", "Unknown error"))
    exit()

# Extract data
times = []
temps = []
for entry in data['list']:
    times.append(datetime.fromtimestamp(entry['dt']))
    temps.append(entry['main']['temp'])

# Visualization
sns.set(style='darkgrid')
plt.figure(figsize=(12, 6))
sns.lineplot(x=times, y=temps, marker='o', color='orange')

plt.title(f'Temperature Forecast for {CITY}', fontsize=16)
plt.xlabel('Date and Time')
plt.ylabel('Temperature (°C)' if UNITS == 'metric' else 'Temperature (°F)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
