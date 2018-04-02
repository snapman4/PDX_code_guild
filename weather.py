import requests

package = {
    'APPID': '0fc45626aecda8d4a8ae32e546356da6', "q": "Portland"

}

r = requests.post('http://api.openweathermap.org/data/2.5/weather', params = package)

#print(r.json())

response = r.json()

# weather_temp = "The current temp Portland is {}.".format(response['main']['temp'])
temp_format = input("Do you want the temperature in Celsius or Fahrenheit? (enter C or F): ").lower()

tempF = int(response['main']['temp'])
tempF = tempF * (9/5) - 459.67
tempF = "{:.2f}".format(tempF)
tempC = int(response['main']['temp'])
tempC = tempC - 273.15
tempC = "{:.2f}".format(tempC)

# print(weather_temp)
if temp_format == "c":
    print("The temperature in Portland is {} degrees Celsius".format(tempC))
elif temp_format == "f":
    print("The temperature in Portland is {} degrees Fahrenheit".format(tempF))


#needs to be converted to F and C
#
# T(°F) = T(K) × 9/5 - 459.67
#
# Example
# Convert 300 Kelvin to degrees Fahrenheit:
#
# T(°F) = 300K × 9/5 - 459.67	= 80.33 °F
#
# T(°C) = T(K) - 273.15
#
# Example
# Convert 300 Kelvin to degrees Celsius:
#
# T(°C) = 300K - 273.15 = 26.85 °C
