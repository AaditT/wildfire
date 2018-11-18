import pyowm
import ulmo
import config
from weatherbit.api import Api
api = Api(config.weatherbit_key)


# GUIDELINES: https://www.ncei.noaa.gov/news/estimating-wildfire-risk-new-tool

def checkWeather():
    owm = pyowm.OWM(config.owm_key)
    observation = owm.weather_at_place('London,GB')
    w = observation.get_weather()
    return [w.get_wind(), w.get_humidity(), w.get_temperature('celsius')]

'''
def checkDrought():
    return ulmo.cpc.drought.get_data(state="CA", climate_division=None, start=None, end=None, as_dataframe=False)
print(checkDrought())
'''

def getPrecipForecast(city, state):
    api.set_granularity('daily')
    forecast = api.get_forecast(city=city, state=state, country="US")
    precip_forecast = forecast.get_series(['precip'])
    print(precip_forecast)
    
 
# getPrecipForecast("San Jose", "CA")
