import logging

from utils.import_dialogue import ImportDialogue

class ReadableTimeOutput():
    _dialogue = None
    requires_and_keyword = False
    nonzero_values_remaining = -1

    def __init__(self):
        ReadableTimeOutput._dialogue = ImportDialogue().import_dialogue("hhmmsswords")

    def output_time(self, stopwatch_time):
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

        seconds_word = (ReadableTimeOutput._dialogue["time"]["second-singular-word"] if seconds == 1 
                        else ReadableTimeOutput._dialogue["time"]["seconds-plural-word"])
        minutes_word = (ReadableTimeOutput._dialogue["time"]["minute-singular-word"] if minutes == 1 
                        else ReadableTimeOutput._dialogue["time"]["minutes-plural-word"])
        hours_word = (ReadableTimeOutput._dialogue["time"]["hour-singular-word"] if hours == 1 
                      else ReadableTimeOutput._dialogue["time"]["hours-plural-word"])

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
        ReadableTimeOutput.nonzero_values_remaining = sum(int(number) > 0 for number in stopwatch_time_output.values())

        if ReadableTimeOutput.nonzero_values_remaining > 1:
            ReadableTimeOutput.requires_and_keyword = True

        time_output += self.add_to_readable_time(stopwatch_time_output["hours"], stopwatch_words["hours_word"])
        time_output += self.add_to_readable_time(stopwatch_time_output["minutes"], stopwatch_words["minutes_word"])
        time_output += self.add_to_readable_time(stopwatch_time_output["seconds"], stopwatch_words["seconds_word"])

        if time_output == "":
            logging.warning("The output in ReadableTimeOutput() is empty.")
            return None
            
        return time_output

    def add_to_readable_time(self, stopwatch_time, stopwatch_words):
        output = ""
        BLANK_SPACE = " "

        if stopwatch_time != 0:
            ReadableTimeOutput.nonzero_values_remaining -= 1
            if ReadableTimeOutput.requires_and_keyword and ReadableTimeOutput.nonzero_values_remaining == 0:
                output += ReadableTimeOutput._dialogue["time"]["and-word"] + BLANK_SPACE
            output += ReadableTimeOutput._dialogue["time"]["time-format"].format(stopwatch_time, stopwatch_words) + BLANK_SPACE
            if ReadableTimeOutput.nonzero_values_remaining == 0:
                output = output.rstrip()

        return output
