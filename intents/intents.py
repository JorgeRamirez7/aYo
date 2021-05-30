from intents.alarm_timer_intents import AlarmTimerIntents
from intents.conversation_intents import ConversationIntents
from intents.music_intents import MusicIntents
from intents.open_documentation_intents import OpenDocumentationIntents
from intents.search_documentation_intents import SearchDocumentationIntents
from intents.stopwatch_intents import StopwatchIntents
from intents.weather_intents import WeatherIntents
from intents.web_search_intents import WebSearchIntents
from utils.find_matching_word import FindMatchingWord
from utils.import_dialogue import ImportDialogue

class Intents():
    """Handles all possible aYo intents that a user may ask"""

    user_queries = ImportDialogue().import_dialogue("intents/user-queries.yaml")

    def intents(self, user_input):
        if FindMatchingWord().get_first_word(user_input, self.user_queries["web-search"]):
            return WebSearchIntents().web_search_intents(user_input)
    
        elif FindMatchingWord().get_first_word(user_input, self.user_queries["open-documentation"]):
            return OpenDocumentationIntents().open_documentation_intents(user_input)

        elif FindMatchingWord().get_first_word(user_input, self.user_queries["search-documentation"]):
            return SearchDocumentationIntents().search_documentation_intents(user_input)

        elif FindMatchingWord().find_match(user_input, self.user_queries["stopwatch"]):
            return StopwatchIntents().stopwatch_intent(user_input)

        elif FindMatchingWord().find_match(user_input, self.user_queries["alarm"]):
            return AlarmTimerIntents().alarm_timer_intent(user_input)
        
        elif FindMatchingWord().find_match(user_input, self.user_queries["music"]):
            return MusicIntents().music_intents(user_input)

        elif FindMatchingWord().find_match(user_input, FindMatchingWord().query["weather"]):
            return WeatherIntents().weahter_intents(user_input)

        else:
            return ConversationIntents().conversation_intents(user_input)
