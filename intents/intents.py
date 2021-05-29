from intents.alarm_timer_intents import AlarmTimerIntents
from intents.conversation_intents import ConversationIntents
from intents.music_intents import MusicIntents
from intents.open_documentation_intents import OpenDocumentationIntents
from intents.search_documentation_intents import SearchDocumentationIntents
from intents.stopwatch_intents import StopwatchIntents
from intents.web_search_intents import WebSearchIntents
from utils.find_matching_word import FindMatchingWord
from utils.import_dialogue import ImportDialogue

class Intents():
    """Handles all possible aYo intents that a user may ask"""

    user_queries = ImportDialogue().import_dialogue("user-queries.yaml")

    def intents(self, user_input):
        key = user_input.split()[0]
        key = key.lower()

        if user_input[-1] == "?" or key == "search":
            return WebSearchIntents().web_search_intents(user_input)
    
        elif key == "open":
            return OpenDocumentationIntents().open_documentation_intents(user_input)

        # probably should change this to use find_match in the future with more language support. works fine for now
        elif key == "c++" or key == "python" or key == "css" or key == "html" or key == "javascript":
            return SearchDocumentationIntents().search_documentation_intents(user_input)

        elif FindMatchingWord().find_match(user_input, self.user_queries["stopwatch"]):
            return StopwatchIntents().stopwatch_intent(user_input)

        elif FindMatchingWord().find_match(user_input, self.user_queries["alarm"]):
            return AlarmTimerIntents().alarm_timer_intent(user_input)
        
        elif FindMatchingWord().find_match(user_input, self.user_queries["music"]):
            return MusicIntents().music_intents(user_input)

        else:
            return ConversationIntents().conversation_intents(user_input)
