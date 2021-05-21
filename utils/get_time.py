"""Extract  time from user input"""
from utils.find_matching_word import FindMatchingWord
from utils.import_dialogue import ImportDialogue

class GetTime():
    _time_values = None

    def __init__(self):
        """Imports time values from a YAML file and stores it in '_time_values'."""
        self._time_values = ImportDialogue().initialize_dialogue('time')

    def get_time(self, user_input:str):
        """Gets the time values (seconds, minutes, hours) from user input.
        
            Args:
                user_input: The string input from a user, which may include time values.

            Returns:
                A dictionary of time values from user_input.
        """

        """Values for both singular and plural are checked in get_time_value()."""
        seconds = self.get_time_value(user_input, self._time_values["second"]["singular"])
        minutes = self.get_time_value(user_input, self._time_values["minute"]["singular"])
        hours = self.get_time_value(user_input, self._time_values["hour"]["singular"])

        time = {
            "seconds": seconds,
            "minutes": minutes,
            "hours": hours
        }

        return time

    def get_time_value(self, user_input:str, time_value:str):
        """Helper class to get the time value of a specific time value. 
           Assumes _time_values follows the format [time_value]["singular" or "plural"].
        
            Args:
                user_input: The string input from a user, which may include time values.
                time_value: The time value that we are checking.

            Returns:
                The value of the time value. Ex. 4 from an input of "4 minutes".
                0 if the time value was not found in the user_input.
        """
        if FindMatchingWord().find_match_single_word(user_input, self._time_values[time_value]["singular"]):
            return FindMatchingWord().get_previous_word(user_input, self._time_values[time_value]["singular"])

        elif FindMatchingWord().find_match_single_word(user_input, self._time_values[time_value]["plural"]):
            return FindMatchingWord().get_previous_word(user_input, self._time_values[time_value]["plural"])

        return 0