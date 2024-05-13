import os

# Function to calculate average temperature for a year
def calculate_average_temperature(year, temperatures):
    total_temp = 0
    num_days = 0
    for temp in temperatures:
        if temp.startswith(year):
            temp_value = int(temp.split(",")[1].rstrip("°C"))
            total_temp += temp_value
            num_days += 1
    if num_days == 0:
        return 0
    return total_temp / num_days

# Function to read temperature data from a file
def read_temperature_data(file_path):
    with open(file_path, "r") as file:
        data = file.read().split()
    return data

# Main function to analyze historical weather data
def analyze_weather_data(directory):
    years_temperatures = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.startswith("weather_data") and filename.endswith(".txt"):
            year = filename.split("_")[1].split(".")[0]
            temperatures = read_temperature_data(os.path.join(directory, filename))
            years_temperatures[year] = temperatures

    # Calculate average temperature for each year
    average_temperatures = {}
    for year, temperatures in years_temperatures.items():
        average_temp = calculate_average_temperature(year, temperatures)
        average_temperatures[year] = average_temp

    # Identify year with highest average temperature
    max_avg_year = max(average_temperatures, key=average_temperatures.get)
    max_avg_temp = average_temperatures[max_avg_year]

    return average_temperatures, max_avg_year, max_avg_temp


directory = "weather_data"
average_temperatures, max_avg_year, max_avg_temp = analyze_weather_data(directory)

# Print results
print("Average Temperatures:")
for year, avg_temp in average_temperatures.items():
    print(f"{year}: {avg_temp}°C")
print(f"\nYear with highest average temperature: {max_avg_year} ({max_avg_temp}°C)")
