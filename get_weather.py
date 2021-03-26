##import requests to send the request to URL
import requests

##IMPORT prettyPrint to convert the JSON to Dictionary
from pprint import pprint

##API KEY FOR OPENWEATHERMAP
API_KEY = 'a7b83c59a2691a35f921a541b802d985'

##GETTING CITY FROM USER
city=input('Enter a City')

##putting API KEY and User's Input in the URL
base_url = 'http://api.openweathermap.org/data/2.5/weather?appid='+API_KEY+'&q='+city

##SENDING request to OpeanWeather and gets The information in json format
weather = requests.get(base_url).json()

##priting the weather using pretty print
pprint(weather)