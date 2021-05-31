from skills.weather_skill import Weather
from utils.find_matching_word import FindMatchingWord

class WeatherIntents:
    def weather_intents(self, ayo_input):
        weather_call = Weather()
        find_word = FindMatchingWord().get_next_word(ayo_input, "weather in")
        return weather_call.Get_Current_Weather(find_word)
