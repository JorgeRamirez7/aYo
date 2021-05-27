"""Convert time values into a readable output."""
import logging

from utils.import_dialogue import ImportDialogue

class ReadableTimeOutput():
    _dialogue = None
    requires_and_keyword = False
    nonzero_values_remaining = -1

    def __init__(self):
        """Imports dialogue for stopwatch values from a YAML file and stores it in '_dialogue'."""
        self._dialogue = ImportDialogue().initialize_dialogue('time')

    def output_time(self, stopwatch_time:dict):
        """Returns a properly formatted time output given a dictionary with time values.
        
            Args:
                stopwatch_time: A dictionary containing only values for 'seconds', 'minutes', and 'hours'.

            Returns:
                The properly formatted time output in the form of a string.
                None if there is an error processing the values in the 'stopwatch_time' dictionary.
        """
        if not ("seconds" in stopwatch_time and 
                "minutes" in stopwatch_time and 
                "hours" in stopwatch_time):
            logging.warning("The dictionary stopwatch_time in ReadableTimeOutput() is missing one or more values.")
            return None

        if (int(stopwatch_time["seconds"]) == 0 and 
            int(stopwatch_time["minutes"]) == 0 and 
            int(stopwatch_time["hours"] == 0)):
            logging.warning("The dictionary stopwatch_time in ReadableTimeOutput() has all zero values.")
            return None

        try:
            is_float = float(stopwatch_time["seconds"]) and float(stopwatch_time["minutes"]) and float(stopwatch_time["hours"])
        except ValueError:
            logging.warning("The dictionary stopwatch_time in ReadableTimeOutput() has one or more non-float values")
            return None

        total_time_in_seconds = int((stopwatch_time["hours"] * 3600) + (stopwatch_time["minutes"] * 60) + stopwatch_time["seconds"])
        minutes, seconds = divmod(total_time_in_seconds, 60)
        hours, minutes = divmod(minutes, 60)

        seconds_word = (self._dialogue["second"]["singular"] if seconds == 1 
                        else self._dialogue["second"]["plural"])
        minutes_word = (self._dialogue["minute"]["singular"] if minutes == 1 
                        else self._dialogue["minute"]["plural"])
        hours_word = (self._dialogue["hour"]["singular"] if hours == 1 
                      else self._dialogue["hour"]["plural"])

        stopwatch_time_output = {
            "seconds": seconds,
            "minutes": minutes,
            "hours": hours
        }

        stopwatch_words = {
            "seconds_word": seconds_word,
            "minutes_word": minutes_word,
            "hours_word": hours_word
        }

        time_output = ""
        self.nonzero_values_remaining = sum(int(number) > 0 for number in stopwatch_time_output.values())

        if self.nonzero_values_remaining > 1:
            self.requires_and_keyword = True

        time_output += self.add_to_readable_time(stopwatch_time_output["hours"], stopwatch_words["hours_word"])
        time_output += self.add_to_readable_time(stopwatch_time_output["minutes"], stopwatch_words["minutes_word"])
        time_output += self.add_to_readable_time(stopwatch_time_output["seconds"], stopwatch_words["seconds_word"])

        if time_output == "":
            logging.warning("The output in ReadableTimeOutput() is empty.")
            return None
            
        return time_output

    def add_to_readable_time(self, stopwatch_time:str, stopwatch_words:str) -> str:
        """Adds the correct time and word for a given time value - 'hours', 'minutes', or 'seconds'.
        
            Args:
                stopwatch_time: A string from a dictionary value for the given time value.
                stopwatch_words: A string from a dictionary value for the given time value's correct word.

            Returns:
                The properly formatted time output in the form of a string.
                An empty string ("") if the given time value is 0. 
        """
        output = ""
        BLANK_SPACE = " "

        if stopwatch_time != 0:
            self.nonzero_values_remaining -= 1
            if self.requires_and_keyword and self.nonzero_values_remaining == 0:
                output += self._dialogue["time-other"]["and"] + BLANK_SPACE
            output += self._dialogue["time-other"]["time-format"].format(stopwatch_time, stopwatch_words) + BLANK_SPACE
            if self.nonzero_values_remaining == 0:
                output = output.rstrip()

        return output
