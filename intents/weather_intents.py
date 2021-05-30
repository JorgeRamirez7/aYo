from weather_skill import Weather
from utils.find_matching_word import FindMatchingWord

class WeatherIntents:
    def weather_intents(self, ayo_input):
        weather_call = Weather()
        return weather_call.Get_Current_Weather(ayo_input)
