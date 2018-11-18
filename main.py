import pyowm
import ulmo

# GUIDELINES: https://www.ncei.noaa.gov/news/estimating-wildfire-risk-new-tool

def checkWeather():
    owm = pyowm.OWM('4ab25daa700e4f5b38ccce7a5c50f9dd')
    observation = owm.weather_at_place('London,GB')
    w = observation.get_weather()
    return [w.get_wind(), w.get_humidity(), w.get_temperature('celsius')]
'''
def checkDrought():
    return ulmo.cpc.drought.get_data(state="CA", climate_division=None, start=None, end=None, as_dataframe=False)
print(checkDrought())
'''
