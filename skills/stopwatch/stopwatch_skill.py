import time
import logging

from utils.readable_time_output import ReadableTimeOutput

_times = {
    "start_time": None,
    "end_time": None
    }

class StopwatchSkill():
    def start_stopwatch(self):
        if _times["start_time"] is None:
            _times["start_time"] = time.time()
            return "Stopwatch has started."
        else:
            return "Stopwatch is already running."

    def stop_stopwatch(self):
        if _times["start_time"] is None:
            return "Try starting a stopwatch first."
        else:
            _times["end_time"] = time.time()
            return self.stopwatch_output()

    def reset_stopwatch(self):
        if _times["start_time"] is None:
            return "There is no stopwatch to reset"

        _times["start_time"] = None
        _times["end_time"] = None
        return "Stopwatch has been reset"

    def stopwatch_output(self):
        if _times["start_time"] is None:
            return "Error. Stopwatch has not started."
        if _times["end_time"] is None:
            return "Error. Stopwatch has not ended."

        seconds_total = _times["end_time"] - _times["start_time"]

        stopwatch_time = {
            "seconds": seconds_total,
            "minutes": 0,
            "hours": 0
        }

        self.reset_stopwatch()
        time_output = ReadableTimeOutput().output_time(stopwatch_time)

        if time_output == None:
            logging.warning("Stopwatch skill received time_output as None.")
            return None

        stopwatch_output = "Stopwatch stopped at {}.".format(time_output)
        return stopwatch_output

    def error(self):
        return "Sorry, Stopwatch is not responding."

    def generic_response(self):
        return "I can create a stopwatch for you. Just say, ayo, start a stopwatch"