<<<<<<< HEAD
import re

class FindMatchingWord(object):
    words_for_start = ['start', 'begin', 'initiate', 'commence', 'set']
    words_for_stop = ['end', 'stop ', 'terminate', 'finish', 'halt', 'conclude', 'close']
    words_for_reset = ['reset', 'cancel']
    words_for_stopwatch = ['stopwatch']
    words_for_timer = ['timer', 'alarm']

    words_for_spotify = ['play', 'next', 'previous', 'pause', 'resume', 'shuffle']

    def find_match(self, input, words_list):
        for word in words_list:
            match_found = re.search(r"\b{}\b".format(word), input, re.IGNORECASE)
            if match_found:
                return True
        return False
=======
"""Search for a given string in a given list."""
import configparser
import re

from utils.import_dialogue import ImportDialogue

class FindMatchingWord():
    query = None

    def __init__(self):
        """Imports text for all queries from a YAML file and stores it in 'query'."""
        config = configparser.ConfigParser()
        config.read('config/ayo.ini')

        user_queries_dialogue_file_name = config.get('dialogue', 'user_queries')
        FindMatchingWord.query = ImportDialogue().import_dialogue(user_queries_dialogue_file_name)

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
>>>>>>> main
