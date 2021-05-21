"""Extract time from user input."""
import logging
import re

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
            "seconds": int(seconds),
            "minutes": int(minutes),
            "hours": int(hours)
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

    def get_clock_time(self, user_input:str):
        """Gets the time from user input when in the form of ##:## AM/PM.
           Time is converted if a single digit hour/minute is present (4 -> 04).
           Time will be AM if not specified to be PM.
        
            Args:
                user_input: The string input from a user, which may include time.

            Returns:
                The time in the form '##:## AM/PM' if found in user_input during regex search.
                None if time is not found in user_input.
        """
        input_time = re.search(r"\d*:\d*(( AM)|( PM))*", user_input, re.IGNORECASE)
        if not input_time:
            logging.warning("get_time did not get a proper time value")
            return None
        else:
            input_time = re.search(r"\d*:\d*(( AM)|( PM))*", user_input, re.IGNORECASE).group(0)
        
        """If time does not contain PM, then it must be AM."""
        contains_PM = re.search(r"\bPM\b", input_time, re.IGNORECASE)

        if contains_PM:
            is_PM = True
        else:
            is_PM = False

        """Adding zero to hour side if it does not follow the following format: ##:## AM/PM"""
        time_hour_side = re.search(r"\d{2}:", input_time, re.IGNORECASE)

        if time_hour_side is None:
            time_hour_side = re.search(r"\d{1}:", input_time, re.IGNORECASE).group(0)
            time_hour = "0" + time_hour_side.rstrip(time_hour_side[-1])
        else:
            time_hour_side = re.search(r"\d{2}:", input_time, re.IGNORECASE).group(0)
            time_hour = time_hour_side.rstrip(time_hour_side[-1])

        """Adding zero to minute side if it does not follow the following format: ##:## AM/PM"""
        time_minute_side = re.search(r":\d{2}", input_time, re.IGNORECASE)

        if time_minute_side is None:
            time_minute_side = re.search(r":\d{1}", input_time, re.IGNORECASE).group(0)
            time_minute = "0" + time_minute_side[1:]
        else:
            time_minute_side = re.search(r":\d{2}", input_time, re.IGNORECASE).group(0)
            time_minute = time_minute_side[1:]

        """The properly formatted time string."""
        time_proper = time_hour + ":" + time_minute

        """Military time."""
        if int(time_hour) > 12:
            return time_proper

        if is_PM:
            time_proper += " PM"
        else:
            time_proper += " AM"

        return time_proper
