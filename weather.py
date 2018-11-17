from weather import Weather, Unit
import openweathermapy.core as owm
import ulmo

class WeatherData():
    def __init__(self, temp, humidity, wind_speed):
        self.temp = temp
        self.humidity = humidity
        self.wind_speed = speed

def checkWeather(zip,state):
    data = owm.get_current(zip=(str(zip)+","+str(state)))
    temp = data.("main.temp")
    humidity = data.("main.humidity")
    speed = data.("main.speed")
    return WeatherData(temp, humidity, speed)
