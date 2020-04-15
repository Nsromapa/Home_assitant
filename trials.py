#Getting long and lati
import geocoder
g = geocoder.ip('me')
loc_ = g.latlng
#print(g.latlng)

#Getting unix stamp
#from datetime import timezone, datetime

#dt = datetime(2015, 10, 19)
#timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
#print(timestamp)
#obs = owm.weather_at_coords(-0.107331,51.503614) 

import pyowm


def weather_condition():
    owm = pyowm.OWM("3055fe5f3b10fc9a5c44ff2d4cab6102")
    print("which city or country do you wish to get their weather info")
    city = input("Input city or country here: ")

    loc = owm.weather_at_place(city)
    weather = loc.get_weather()

    temp = weather.get_temperature(unit="celsius")
    print("the temperature in"+" "+city+" "+"is"+ str(temp))


def weather_fore(location):
    owm = pyowm.OWM("3055fe5f3b10fc9a5c44ff2d4cab6102")
    fc = owm.daily_forecast(location, limit=2)
    f = fc.get_forecast()
    print(f)


weather_fore('accra')






