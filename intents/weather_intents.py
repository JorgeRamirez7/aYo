from skills.weather_skill import Weather
from utils.find_matching_word import FindMatchingWord
from utils.import_dialogue import ImportDialogue

class WeatherIntents:
    def weather_intents(self, ayo_input):
        weather_in_queries = ImportDialogue().import_dialogue("intents/weather.yaml")
        weather_call = Weather()
        
        if FindMatchingWord().get_next_word(ayo_input, weather_in_queries["weather-in"]):
            find_word = FindMatchingWord().get_next_word(ayo_input, weather_in_queries["weather-in"])
            return weather_call.Get_Current_Weather(find_word)

        else:
            """The default location for weather is Seattle - if user does not specify city."""
            return weather_call.Get_Current_Weather("Seattle")