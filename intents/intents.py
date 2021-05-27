"""Handles all possible aYo intents that a user may ask"""
from intents.alarm_timer_intents import AlarmTimerIntents
from intents.music_intents import MusicIntents
from intents.open_documentation_intents import OpenDocumentationIntents
from intents.search_documentation_intents import SearchDocumentationIntents
from intents.stopwatch_intents import StopwatchIntents
from intents.web_search_intents import WebSearchIntents
from utils.find_matching_word import FindMatchingWord
from utils.import_dialogue import ImportDialogue

class Intents():
    def __init__(self):
        self.user_queries = ImportDialogue().import_dialogue("user-queries.yaml")
        self.jokes_queries = ImportDialogue().import_dialogue("casual/jokes.yaml")
        self.greetings_queries = ImportDialogue().import_dialogue("casual/greetings.yaml")

    def intents(self, user_input):
        if user_input[-1] == '?' or user_input.split()[0] == "Search":
            return WebSearchIntents().web_search_intents(user_input)
    
        elif user_input.split()[0] == "Open":
            return OpenDocumentationIntents().open_documentation_intents(user_input)

        elif user_input.split()[0] == "C++" or user_input.split()[0] == "Python":
            return SearchDocumentationIntents().search_documentation_intents(user_input)

        elif FindMatchingWord().find_match(user_input, self.user_queries["stopwatch"]):
            return StopwatchIntents().stopwatch_intent(user_input)

        elif FindMatchingWord().find_match(user_input, self.user_queries["alarm"]):
            return AlarmTimerIntents().alarm_timer_intent(user_input)
        
        elif FindMatchingWord().find_match(user_input, self.user_queries["music"]):
            return MusicIntents().music_intents(user_input)

        elif FindMatchingWord().find_match(user_input, self.jokes_queries["user-trigger"]):
            return "Jokes placeholder"

        elif FindMatchingWord().find_match(user_input, self.greetings_queries["user-trigger"]):
            return "Greetings placeholder"

        else:
            return "Hmm, I don't understand that"
