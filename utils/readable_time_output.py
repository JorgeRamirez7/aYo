import logging
import yaml

_dialogue = None
requires_and_keyword = False
nonzero_values_remaining = -1

class ReadableTimeOutput():
    def __init__(self):
        global _dialogue

        try:
            with open("dialogue\en_US\hhmmsswords.yaml") as file:
                _dialogue = yaml.load(file, Loader=yaml.FullLoader)
        except:
            logging.warning("Could not load dialogue for ReadableTimeOutput.")

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

        global requires_and_keyword, nonzero_values_remaining
        total_time_in_seconds = int((stopwatch_time["hours"] * 3600) + (stopwatch_time["minutes"] * 60) + stopwatch_time["seconds"])
        minutes, seconds = divmod(total_time_in_seconds, 60)
        hours, minutes = divmod(minutes, 60)

        seconds_word = (_dialogue["time"]["second-singular-word"] if seconds == 1 else _dialogue["time"]["seconds-plural-word"])
        minutes_word = (_dialogue["time"]["minute-singular-word"] if minutes == 1 else _dialogue["time"]["minutes-plural-word"])
        hours_word = (_dialogue["time"]["hour-singular-word"] if hours == 1 else _dialogue["time"]["hours-plural-word"])

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
        nonzero_values_remaining = sum(int(number) > 0 for number in stopwatch_time_output.values())

        if nonzero_values_remaining > 1:
            requires_and_keyword = True

        time_output += self.add_to_readable_time(stopwatch_time_output["hours"], stopwatch_words["hours_word"])
        time_output += self.add_to_readable_time(stopwatch_time_output["minutes"], stopwatch_words["minutes_word"])
        time_output += self.add_to_readable_time(stopwatch_time_output["seconds"], stopwatch_words["seconds_word"])

        if time_output == "":
            logging.warning("The output in ReadableTimeOutput() is empty.")
            return None
            
        return time_output

    def add_to_readable_time(self, stopwatch_time, stopwatch_words):
        global requires_and_keyword, nonzero_values_remaining
        output = ""

        if stopwatch_time != 0:
            nonzero_values_remaining -= 1
            if requires_and_keyword and nonzero_values_remaining == 0:
                output += _dialogue["time"]["and-word"]
            output += _dialogue["time"]["time-format"].format(stopwatch_time, stopwatch_words)
            if nonzero_values_remaining == 0:
                output = output.rstrip()

        return output