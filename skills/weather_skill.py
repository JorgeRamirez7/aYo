import configparser
import logging
import requests, json, math

from pathlib import Path
from playsound import playsound

from skills.random_element_skill import RandomElementSkill
from utils.import_dialogue import ImportDialogue

class Weather:
    """
     This is a Python program to find current weather details of any city
     using openweathermap api

     function getCurrentWeather("City Name Here") is the only method needed
        it returns the current temperature in the city input into this function
        it will just return just the the number as an interger however.
    """

    _dialogue = ImportDialogue().import_dialogue(Path("skills/weather.yaml"))
    _random_weather_forecast = RandomElementSkill(_dialogue["weather"])
    _error_api_sfx = str(Path("data/warning_openweather_api_missing.mp3"))

    # Configuration settings
    try:
        config = configparser.ConfigParser()
        config.read('config/config.ini')
        openweather_api_key = config.get('openweather', 'key')
    except:
        logging.warning("There is no 'openweather' or 'key' value in 'config/config.ini'")
        openweather_api_key = ""

    def Get_Current_Weather(self, the_city_name):
        # this is where the api key goes
        api_key = self.openweather_api_key

        # this is where the base url for the site you are getting your info from goes
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # the city name as parameter
        city_name = the_city_name

        # the compleate url which is variable to cite
        # complete url address which works with openweathermap.org
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        # get method of requests module
        # returns the response object
        # in this case the data about the weather in a certain city
        response = requests.get(complete_url)

        # json method of response object
        # converts a json formated data into python formated data
        x = response.json()

        # x contains the list of nested dictionaries

        # invalid API key
        if x["cod"] == 401:
            logging.warning("No valid OpenWeather API key found within config/config.ini")
            playsound(str(self._error_api_sfx))
            return None

        # Check the value of "cod" key is equal to "404",
        # which means the city is found
        # Otherwise the city is not found
        if x["cod"] != "404":

            # store the value of "main"
            # key in variable y
            y = x["main"]

            # store the value corresponding to the "temp" key of y
            # note: y["temp"] returns the temperature in kelvins
            #        thus the formula (K - 275.15) * 9/5 + 32
            #        was used to convert to Farenheight
            current_temperature = y["temp"]
            updated_temperature = math.trunc((float(current_temperature) - 275.15) * (9/5) + 32)

            # store the value corresponding to the "pressure" key of y
            # probably will not use that
            # current_pressure = y["pressure"]

            # store the value corresponding to the "humidity" key of y
            # current_humidiy = y["humidity"]

            # store the value of "weather key in variable z
            z = x["weather"]

            # store the value corresponding to the "description" key at
            #   the 0th index of z
            weather_description = z[0]["description"]

            weather_forecast = self._random_weather_forecast.get_random_element().format(city_name, weather_description, str(updated_temperature))
            return weather_forecast

        else:
            return self._dialogue["error"].format(city_name)
