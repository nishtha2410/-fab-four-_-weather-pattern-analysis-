import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate a date range
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

# Simulate temperature data (in degrees Celsius)
# Assume a seasonal pattern with some random noise
temperature_mean = 20  # Average temperature
temperature_amplitude = 10  # Amplitude of seasonal variation
temperature_noise = np.random.normal(0, 2, len(dates))  # Random noise
temperature = temperature_mean + temperature_amplitude * np.sin(2 * np.pi * (dates.dayofyear - 80) / 365) + temperature_noise

# Simulate rainfall data (in mm)
# Assume more rainfall in the summer months and less in the winter
rainfall_mean = 5  # Average rainfall
rainfall_amplitude = 15  # Amplitude of seasonal variation
rainfall_noise = np.random.normal(0, 2, len(dates))  # Random noise
rainfall = rainfall_mean + rainfall_amplitude * np.sin(2 * np.pi * (dates.dayofyear - 80) / 365) + rainfall_noise

# Ensure no negative rainfall values
rainfall = np.maximum(rainfall, 0)

# Create a DataFrame
weather_data = pd.DataFrame({
    'Date': dates,
    'Temperature': temperature,
    'Rainfall': rainfall
})

# Plotting
plt.figure(figsize=(14, 6))

# Plot Temperature
plt.subplot(2, 1, 1)
plt.plot(weather_data['Date'], weather_data['Temperature'], color='orange', label='Temperature (°C)')
plt.title('Simulated Daily Temperature Patterns for 2023')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid()
plt.legend()

# Plot Rainfall
plt.subplot(2, 1, 2)
plt.bar(weather_data['Date'], weather_data['Rainfall'], color='blue', label='Rainfall (mm)', width=1.0)
plt.title('Simulated Daily Rainfall Patterns for 2023')
plt.xlabel('Date')
plt.ylabel('Rainfall (mm)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()