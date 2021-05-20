"""Search for a given string in a given list."""
import re

from utils.import_dialogue import ImportDialogue

class FindMatchingWord():
    query = None

    def __init__(self):
        """Imports text for all queries from a YAML file and stores it in 'query'."""
        FindMatchingWord.query = ImportDialogue().initialize_dialogue('user_queries')

    def find_match(self, input:str, words_list:str) -> bool:
        """Searches for a given input in a given list of words.
        
            Args:
                input: The string input from a user, indicating their desired aYo action.
                words_list: The dictionary of strings to search for 'input' in.

            Returns:
                True if the input was found in the list of words.
                False if the input was not found in the list of words.
        """
        for word in words_list:
            match_found = re.search(r"\b{}\b".format(word), input, re.IGNORECASE)
            
            if match_found:
                return True
        
        return False
