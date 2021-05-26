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

        try:
            time = {
                "seconds": int(seconds),
                "minutes": int(minutes),
                "hours": int(hours)
            }

        except:
            logging.warning("Did not receive a number value in get_time.")
            return None

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
        """Helper class to get the time from user input when in the form of ##:## AM/PM.
           Time is converted if a single digit hour/minute is present (4 -> 04).
           Time will be AM if not specified to be PM.
        
            Args:
                user_input: The string input from a user, which may include time.

            Returns:
                A dictionary of clock values containing the string time_proper, bool is_PM, int minutes, and int hours.
                None if time is not found in user_input.
        """
        input_time = re.search(r"\d*:\d*(( AM)|( PM))*", user_input, re.IGNORECASE)
        if not input_time:
            logging.warning("get_time did not get a proper time value")
            return None
        else:
            input_time = re.search(r"\d*:\d*(( AM)|( PM))*", user_input, re.IGNORECASE).group(0)

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

        """If time does not contain PM, then it must be AM."""
        contains_PM = re.search(r"\bPM\b", input_time, re.IGNORECASE)

        if contains_PM:
            is_PM = True
        else:
            is_PM = False

        """The properly formatted time string."""
        time_proper = time_hour + ":" + time_minute

        """Military time."""
        if int(time_hour) > 12:
            return time_proper

        clock_values = {
            "time_proper": time_proper,
            "is_PM": is_PM,
            "minutes": int(time_minute),
            "hours": int(time_hour)
        }

        return clock_values

    def get_clock_time_string(self, user_input:str):
        """Gets the string time from user input when in the form of ##:## AM/PM.
        
            Args:
                user_input: The string input from a user, which may include time.

            Returns:
                The time in the form '##:## AM/PM' if found in user_input during regex search.
                None if time is not found in user_input.
        """
        clock_values = self.get_clock_time(user_input)

        if clock_values is None:
            return None
        
        time_proper = clock_values["time_proper"]
        is_PM = clock_values["is_PM"]

        if is_PM:
            time_proper += " PM"
        else:
            time_proper += " AM"

        return time_proper

    def get_clock_time_dict(self, user_input:str):
        """Gets the dictionary of time values from user input when in the form of ##:## AM/PM.
        
            Args:
                user_input: The string input from a user, which may include time.

            Returns:
                A dictionary of time values - containing seconds, minutes, and hours.
                None if time is not found in user_input.
        """
        clock_values = self.get_clock_time(user_input)

        if clock_values is None:
            return None

        time_hour = clock_values["hours"]
        time_minute = clock_values["minutes"]
        is_PM = clock_values["is_PM"]

        """If it is 12:## AM, set hour to 00:##"""
        if time_hour == 12 and not is_PM:
            time_hour = 0

        if is_PM:
            time_hour = time_hour + 12

        user_time = {
            "seconds": 0,
            "minutes": time_minute,
            "hours": time_hour
        }

        return user_time

    def get_seconds_from_time(self, user_time:dict):
        """Gets the total number of seconds from a user_time dictionary containing seconds, minutes, and hours values.
        
            Args:
                user_time: A time dictionary containing values "seconds", "minutes", and "hours" with float values.

            Returns:
                The total time in seconds of the given time dictionary.
                None if the given time dictionary is not a valid format.
        """
        if not ("seconds" in user_time and 
                "minutes" in user_time and 
                "hours" in user_time):
            logging.warning("The dictionary time in GetTime() is missing one or more values.")
            return None

        try:
            is_float = float(user_time["seconds"]) and float(user_time["minutes"]) and float(user_time["hours"])
        except ValueError:
            logging.warning("The dictionary time in GetTime() has one or more non-float values")
            return None

        return user_time["seconds"] + (user_time["minutes"] * 60) + (user_time["hours"] * 3600)
