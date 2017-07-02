#!/home/gerardo/anaconda2/bin/python
import redis
import json
import urllib
import urllib2
import re
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import ConfigParser

# Get our configs
config = ConfigParser.ConfigParser()
config.read('.env')

WEATHER_API_KEY = config.get("api_keys", "WEATHER_API_KEY")
api_url = config.get('urls','api_url')
redis_host = config.get('redis','host')
redis_port = config.get('redis','port')
weather_file = config.get('files','weather_file')

r = redis.Redis(host=redis_host, port=int(redis_port), db=0)


def store_weather(weather_data):
    city = weather_data.keys()[0]
    r.set(city, weather_data[city])

def get_weather(city):
    query = urllib.quote(city)
    url = api_url.format(query)
    results = urllib2.urlopen(url).read()
    
    weather_data = {query: results}

    store_weather(weather_data)

    return weather_data

def generate_graph():
    cities = r.keys()

    temps = []

    for key in cities:
        result = r.get(key)
        parsed = json.loads(result)
        temps.append(parsed['main']['temp_max'])
           
    y_pos = np.arange(len(cities))
    
    plt.bar(y_pos, temps, align='center', alpha=0.5)
    plt.xticks(y_pos, cities)
    plt.ylabel('Temperatures (in F)')
    plt.title('Temperatures across different cities.')

    plt.savefig(weather_file)

#print get_weather('london')
generate_graph()
