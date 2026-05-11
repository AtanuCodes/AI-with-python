# Temperature Advisor
# Task:
# Ask the user for the current temperature in Celsius and the weather condition (sunny, rainy, snowy, cloudy).
# Then give advice based on both temperature and condition using conditionals.
# Examples of advice:

# Temp > 30 and sunny → "It's very hot! Stay hydrated and avoid direct sun."
# Temp < 0 and snowy → "Heavy snow! Better stay indoors."
# 15-25 and sunny → "Perfect weather for a walk!"

# Make at least 6-8 different combinations.

weather_condition = input("Enter the current weather condition (sunny, rainy, snowy, cloudy): ").lower()
if weather_condition not in ['sunny', 'rainy', 'snowy', 'cloudy']:
    print("Invalid weather condition. Please enter sunny, rainy, snowy, or cloudy.")
    exit()
temperature_celsius = float(input("Enter the current temperature in Celsius: "))

if temperature_celsius > 30 and weather_condition == 'sunny':
    print("It's very hot! Stay hydrated and avoid direct sun.")
elif temperature_celsius < 0 and weather_condition == 'snowy':
    print("Heavy snow! Better stay indoors.")
elif 15 <= temperature_celsius <=25 and weather_condition == 'sunny':
    print("Perfect weather for a walk!")
elif temperature_celsius < 0 and weather_condition == 'cloudy':
    print("It's cold and cloudy. Bundle up!")
elif temperature_celsius > 30 and weather_condition == 'rainy':
    print("It's hot and rainy. Stay cool and dry.")
elif 0 <= temperature_celsius <= 15 and weather_condition == 'snowy':
    print("It's snowing and cold. Dress warmly!")
elif 25 < temperature_celsius < 30 and weather_condition == 'rainy':
    print("It's warm and rainy. Carry an umbrella.")
else:
    print("The weather is moderate. Enjoy your day!")


  