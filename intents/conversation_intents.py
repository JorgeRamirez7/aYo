from skills.random_element_skill import RandomElementSkill
from utils.find_matching_word import FindMatchingWord
from utils.import_dialogue import ImportDialogue

class ConversationIntents():
    jokes_queries = ImportDialogue().import_dialogue("conversation/jokes.yaml")
    greetings_queries = ImportDialogue().import_dialogue("conversation/greetings.yaml")
    ayo_functions_queries = ImportDialogue().import_dialogue("conversation/ayo-functions.yaml")
    unknown_queries = ImportDialogue().import_dialogue("conversation/unknown.yaml")

    jokes = RandomElementSkill(jokes_queries["program-response"])
    greetings = RandomElementSkill(greetings_queries["program-response"])
    ayo_functions = RandomElementSkill(ayo_functions_queries["program-response"])
    unknown = RandomElementSkill(unknown_queries["program-response"])

    def conversation_intents(self, user_input:str) -> str:
        """Performs an action given a Conversation intent.
        
            Args:
                user_input: The string input from a user, potentially indicating a Conversation action.

            Returns:
                A Conversation response string for aYo to speak/display.
        """
        if FindMatchingWord().find_match(user_input, self.jokes_queries["user-trigger"]):
            return self.jokes.get_random_element()
        
        elif FindMatchingWord().find_match(user_input, self.greetings_queries["user-trigger"]):
            return self.greetings.get_random_element()

        elif FindMatchingWord().find_match(user_input, self.ayo_functions_queries["user-trigger"]):
            return self.ayo_functions.get_random_element()

        else:
            return self.unknown.get_random_element()
