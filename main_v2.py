from weatherbit.api import Api
import config

api = Api(config.weatherbit_key)

class WeatherData:

    def __init__(self, city, state):
        self.city = city
        self.state = state

    def getPrecip(self):
        api.set_granularity('daily')
        forecast = api.get_forecast(city=self.city, state=self.state, country="US")
        precip_forecast = forecast.get_series(['precip'])
        print(precip_forecast)

    def getWindSpeed(self):
        api.set_granularity('daily')
        forecast = api.get_forecast(city=self.city, state=self.state, country="US")
        wind_spd_forecast = forecast.get_series(['wind_spd'])
        print(wind_spd_forecast)

    def getWindDir(self):
        api.set_granularity('daily')
        forecast = api.get_forecast(city=self.city, state=self.state, country="US")
        wind_dir_forecast = forecast.get_series(['wind_dir'])
        print(wind_dir_forecast)

    def getTemp(self):
        api.set_granularity('daily')
        forecast = api.get_forecast(city=self.city, state=self.state, country="US")
        temp_forecast = forecast.get_series(['temp'])
        print(temp_forecast)

    def getHumid(self):
        api.set_granularity('daily')
        forecast = api.get_forecast(city=self.city, state=self.state, country="US")
        rh_forecast = forecast.get_series(['rh'])
        print(rh_forecast)

"""
myData = WeatherData("San Jose", "CA")
myData.getPrecip()
myData.getWindSpeed()
myData.getWindDir()
myData.getTemp()
myData.getHumid()
"""
