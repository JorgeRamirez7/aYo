from skills.random_element_skill import RandomElementSkill
from utils.find_matching_word import FindMatchingWord
from utils.import_dialogue import ImportDialogue

class CasualIntents():
    jokes_queries = ImportDialogue().import_dialogue("casual/jokes.yaml")
    greetings_queries = ImportDialogue().import_dialogue("casual/greetings.yaml")

    jokes = RandomElementSkill(jokes_queries["program-response"])
    greetings = RandomElementSkill(greetings_queries["program-response"])

    def casual_intents(self, user_input:str) -> str:
        """Performs an action given a Casual intent.
        
            Args:
                user_input: The string input from a user, potentially indicating a Casual action.

            Returns:
                A Casual response string for aYo to speak/display.
        """
        if FindMatchingWord().find_match(user_input, self.jokes_queries["user-trigger"]):
            return self.jokes.get_random_element()
        
        elif FindMatchingWord().find_match(user_input, self.greetings_queries["user-trigger"]):
            return self.greetings.get_random_element()
