import pyowm
from pyowm import OWM
import config

city = input('Город?: ')
owm = OWM(config.TOKEN)
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather
w.temperature('celsius')['temp']
print (w)