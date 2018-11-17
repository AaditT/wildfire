from weather import Weather, Unit
import yweather
#import openweathermapy.core as owm
#import ulmo

# https://ulmo.readthedocs.io/en/latest/api.html#module-ulmo.cpc.drought


client = yweather.Client()
def get_weather_data(location):
    return client.fetch_weather(client.fetch_woeid(location))
print(get_weather_data('Oslo, Norway'))

#def droughtData(state):
#    ulmo.cpc.drought.get_data(state=state, climate_division=None, start="01/01/2018", end="11/17/2018", as_dataframe=False)
''' WACK APIs
def checkWeather(zip,state):
    settings = {"APPID": "4ab25daa700e4f5b38ccce7a5c50f9dd", "units": "metric"}
    data = owm.get_current((str(zip)+","+str(state)), **settings)
    temp = data("main.temp")
    humidity = data("main.humidity")
    speed = data("main.speed")
    return [temp, humidity, speed]
print(checkWeather(95135, "CA"))
print(droughtData("CA"))

weather = Weather(unit=Unit.CELSIUS)
lookup = weather.lookup_by_location('san jose')
condition = lookup.condition
print(condition)
print(condition.text)
'''
