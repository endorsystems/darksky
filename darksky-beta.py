################################################################################
#  Darksky.net API call for downloaded weather for use in an application.      #
#  Written in Python 3, no requirements other then the import.                 #
################################################################################
import requests
import sys
import csv
import json
import os.path

# Pulling DarkSky API data, translating it (pulling JSON tags), and dumping it
# into a database
# TODO: Class with object oriented stuff?

# Check if config is present
if os.path.exists("skynet_locations")==True:
    continue
elif os.path.exists("skynet_api")==True:
    continue
else:
    sys.exit("Files missing") # TODO best to have the user setup the files...

# Setting up config
saved_latitude =
saved_longitude =
saved_api_key =

# Default Darksky pulling
def skynet(la, lo, api_key):
    latitude = la
    longitude = lo
    skykey = api_key

    url = "https://api.darksky.net/forecast/[skykey]/[latitude,longitude]"
    # Marking required values from Darksky JSON output
    # ['currently','hourly','daily','timezone']
    json_data = json.loads(url)
    weather_data = weather_parsed['currently','hourly','daily','timezone']
    # Open csv file for writing
    sky_data = open('darksky_data.csv', 'w')
    csvwriter = csv.writer(sky_data)
    count = 0
    for weather in weather_data:
        if count == 0:
            header = weather.keys()
            csvwriter.writerow(header)
            count +=1
        csvwriter.writerow(weather.values())
    sky_data.close()


# Calling the function with the saved items into a variable
forcast = skynet(saved_latitude, saved_langitude, saved_api_key)


