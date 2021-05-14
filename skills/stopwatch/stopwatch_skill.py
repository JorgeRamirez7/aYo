import logging
import time
import yaml

from utils.readable_time_output import ReadableTimeOutput

_times = {
    "start_time": None,
    "end_time": None
    }

_dialogue = None

class StopwatchSkill():
    def __init__(self):
        global _dialogue

        try:
            with open("dialogue\en_US\stopwatch.yaml") as file:
                _dialogue = yaml.load(file, Loader=yaml.FullLoader)
        except:
            logging.warning("Could not load dialogue for Stopwatch.")

    def start_stopwatch(self):
        if _times["start_time"] is None:
            _times["start_time"] = time.time()
            return _dialogue["user-start"]["success-started"]
        else:
            return _dialogue["user-start"]["error-already-running"]

    def stop_stopwatch(self):
        if _times["start_time"] is None:
            return _dialogue["user-stop"]["error-hasnt-been-started"]
        else:
            _times["end_time"] = time.time()
            return self.stopwatch_output()

    def reset_stopwatch(self):
        if _times["start_time"] is None:
            return _dialogue["user-reset"]["error-no-stopwatch-available"]

        _times["start_time"] = None
        _times["end_time"] = None
        return _dialogue["user-reset"]["success-reset"]

    def stopwatch_output(self):
        if _times["start_time"] is None:
            logging.warning("Stopwatch has not started.")
            return None
        if _times["end_time"] is None:
            logging.warning("Stopwatch has not ended.")
            return None

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

        stopwatch_output = _dialogue["program-output"]["stopped-at"].format(time_output)
        return stopwatch_output

    def error(self):
        return _dialogue["program-error"]["error-not-responding"]

    def generic_response(self):
        return _dialogue["user-generic"]["response"]
