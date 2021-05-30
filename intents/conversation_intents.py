from skills.random_element_skill import RandomElementSkill
from utils.find_matching_word import FindMatchingWord
from utils.import_dialogue import ImportDialogue

class ConversationIntents():
    """Handles Conversation intents that a user may ask"""
    conversation_queries = ImportDialogue().import_dialogue("intents/conversation-queries.yaml")

    jokes_queries = ImportDialogue().import_dialogue("conversation/jokes.yaml")
    fun_facts_queries = ImportDialogue().import_dialogue("conversation/fun-facts.yaml")
    greetings_queries = ImportDialogue().import_dialogue("conversation/greetings.yaml")
    thanks_queries = ImportDialogue().import_dialogue("conversation/thanks.yaml")
    ayo_functions_queries = ImportDialogue().import_dialogue("conversation/ayo-functions.yaml")
    credits_queries = ImportDialogue().import_dialogue("conversation/credits.yaml")
    how_am_i_queries = ImportDialogue().import_dialogue("conversation/how-am-i.yaml")
    user_apologies_queries = ImportDialogue().import_dialogue("conversation/user-apologies.yaml")
    bye_queries = ImportDialogue().import_dialogue("conversation/bye.yaml")
    unknown_queries = ImportDialogue().import_dialogue("conversation/unknown.yaml")

    jokes = RandomElementSkill(jokes_queries["program-response"])
    fun_facts = RandomElementSkill(fun_facts_queries["program-response"])
    greetings = RandomElementSkill(greetings_queries["program-response"])
    thanks = RandomElementSkill(thanks_queries["program-response"])
    ayo_functions = RandomElementSkill(ayo_functions_queries["program-response"])
    credits = RandomElementSkill(credits_queries["program-response"])
    how_am_i = RandomElementSkill(how_am_i_queries["program-response"])
    user_apologies = RandomElementSkill(user_apologies_queries["program-response"])
    bye = RandomElementSkill(bye_queries["program-response"])
    unknown = RandomElementSkill(unknown_queries["program-response"])

    def conversation_intents(self, user_input:str) -> str:
        """Performs an action given a Conversation intent.
        
            Args:
                user_input: The string input from a user, potentially indicating a Conversation action.

            Returns:
                A Conversation response string for aYo to speak/display.
        """
        if FindMatchingWord().find_match(user_input, self.conversation_queries["joke"]):
            return self.jokes.get_random_element()
        
        if FindMatchingWord().find_match(user_input, self.conversation_queries["fun-fact"]):
            return self.fun_facts.get_random_element()

        elif FindMatchingWord().find_match(user_input, self.conversation_queries["greeting"]):
            return self.greetings.get_random_element()

        elif FindMatchingWord().find_match(user_input, self.conversation_queries["thanks"]):
            return self.thanks.get_random_element()

        elif FindMatchingWord().find_match(user_input, self.conversation_queries["ayo-functions"]):
            return self.ayo_functions.get_random_element()
        
        elif FindMatchingWord().find_match(user_input, self.conversation_queries["credits"]):
            return self.credits.get_random_element()

        elif FindMatchingWord().find_match(user_input, self.conversation_queries["how-am-i"]):
            return self.how_am_i.get_random_element()

        elif FindMatchingWord().find_match(user_input, self.conversation_queries["user-apologies"]):
            return self.user_apologies.get_random_element()

        elif FindMatchingWord().find_match(user_input, self.conversation_queries["bye"]):
            return self.bye.get_random_element()

        else:
            return self.unknown.get_random_element()
