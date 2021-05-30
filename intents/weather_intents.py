from skills.weather_skill import Weather
from utils.find_matching_word import FindMatchingWord

class WeatherIntents:
    def weather_intents(self, ayo_input):
        weather_call = Weather()
        find_word = find_matching_word().get_word_after_weather_in(ayo_input)
        return weather_call.Get_Current_Weather(find_word)
