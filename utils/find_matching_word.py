import logging
import re

from utils.import_dialogue import ImportDialogue

class FindMatchingWord():
    """Search for a given string in a given list."""
    query = None

    def __init__(self):
        """Imports text for all queries from a YAML file and stores it in 'query'."""
        FindMatchingWord.query = ImportDialogue().import_dialogue("user-queries.yaml")

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

    def find_match_single_word(self, input:str, single_word:str) -> bool:
        """Searches and determines if input is equal to a single_word.
        
            Args:
                input: The string input from a user.
                single_word: The word we are comparing input with.

            Returns:
                True if the input matches the single_word.
                False if the input does not match the single_word.
        """
        word_found = re.search(r"\b{}\b".format(single_word), input, re.IGNORECASE)

        if word_found:
            return True

        return False

    def get_previous_word(self, input:str, word_search:str):
        """Searches for the word before a given word in an input.
        
            Args:
                input: The string input from a user.
                word_search: The word that is being searched.

            Returns:
                The word before 'word_search' if found during regex search.
                None if the word before 'word_search' is not found.
        """
        try:
            return re.search(r"\w+(?=\s+{})".format(word_search), input, re.IGNORECASE).group(0)

        except:
            logging.warning("get_previous_word in FindMatchingWord could not find a match.")
            return False

    def get_next_word(self, input:str, word_search:str):
        """Searches for the word after a given word in an input.
        
            Args:
                input: The string input from a user.
                word_search: The word that is being searched.

            Returns:
                The word after 'word_search' if found during regex search.
                None if the word after 'word_search' is not found.
        """
        try:
            return re.search(r"(?<={}\s)[^.\s!?]*".format(word_search), input, re.IGNORECASE).group(0)

        except:
            logging.warning("get_next_word in FindMatchingWord could not find a match.")
            return False

    def get_first_word(self, input:str, words_list:str):
        """Searches for the word word_search in the first word of an input.
        
            Args:
                input: The string input from a user.
                word_search: The word that is being searched.

            Returns:
                The word 'word_search' if found during regex search.
                None if the word 'word_search' is not found as the first input of string input.
        """
        first_word = input.split()[0]
        first_word = first_word.lower()

        for word in words_list:
            if first_word == word.lower():
                return True
            
        return False
