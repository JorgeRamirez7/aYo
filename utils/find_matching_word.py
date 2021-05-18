import re

from utils.import_dialogue import ImportDialogue

class FindMatchingWord(object):
    query = None

    def __init__(self):
        FindMatchingWord.query = ImportDialogue().import_dialogue("userqueries.yaml")

    def find_match(self, input, words_list):
        for word in words_list:
            match_found = re.search(r"\b{}\b".format(word), input, re.IGNORECASE)
            
            if match_found:
                return True
        
        return False
