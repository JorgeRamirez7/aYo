"""Extract  time from user input"""
import re

from utils.find_matching_word import FindMatchingWord
from utils.import_dialogue import ImportDialogue

class GetTime():
    _time_values = None

    def __init__(self):
        """Imports time values from a YAML file and stores it in '_time_values'."""
        self._time_values = ImportDialogue().initialize_dialogue('time')

    def get_time(self, user_input:str):
        seconds = 0
        minutes = 0
        hours = 0

        if FindMatchingWord().find_match_single_word(user_input, self._time_values["second"]["singular"]):
            seconds = FindMatchingWord().get_previous_word(user_input, self._time_values["second"]["singular"])
        elif FindMatchingWord().find_match_single_word(user_input, self._time_values["second"]["plural"]):
            seconds = FindMatchingWord().get_previous_word(user_input, self._time_values["second"]["plural"])
        
        if FindMatchingWord().find_match_single_word(user_input, self._time_values["minute"]["singular"]):
            minutes = FindMatchingWord().get_previous_word(user_input, self._time_values["minute"]["singular"])
        elif FindMatchingWord().find_match_single_word(user_input, self._time_values["minute"]["plural"]):
            minutes = FindMatchingWord().get_previous_word(user_input, self._time_values["minute"]["plural"])

        if FindMatchingWord().find_match_single_word(user_input, self._time_values["hour"]["singular"]):
            hours = FindMatchingWord().get_previous_word(user_input, self._time_values["hour"]["singular"])
        elif FindMatchingWord().find_match_single_word(user_input, self._time_values["hour"]["plural"]):
            hours = FindMatchingWord().get_previous_word(user_input, self._time_values["hour"]["plural"])

        time = {
            "seconds": seconds,
            "minutes": minutes,
            "hours": hours
        }

        return time

