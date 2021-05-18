"""Perform Stopwatch intents."""
import configparser
import logging
import time

from utils.import_dialogue import ImportDialogue
from utils.readable_time_output import ReadableTimeOutput

class StopwatchSkill():
    _dialogue = None
    _times = {
    "start_time": None,
    "end_time": None
    }

    def __init__(self):
        """Imports dialogue for stopwatch from a YAML file and stores it in '_dialogue'."""
        config = configparser.ConfigParser()
        config.read('config/ayo.ini')

        stopwatch_dialogue_file_name = config.get('dialogue', 'stopwatch')
        self._dialogue = ImportDialogue().import_dialogue(stopwatch_dialogue_file_name)

    def start_stopwatch(self) -> str:
        """Starts Stopwatch by storing the current time and returns a Stopwatch status string."""
        if self._times["start_time"] is None:
            self._times["start_time"] = time.time()
            return self._dialogue["user-start"]["success-started"]
        else:
            return self._dialogue["user-start"]["error-already-running"]

    def stop_stopwatch(self) -> str:
        """Stops Stopwatch by storing the current time and returns a stopwatch time string."""
        if self._times["start_time"] is None:
            return self._dialogue["user-stop"]["error-hasnt-been-started"]
        else:
            self._times["end_time"] = time.time()
            return self.stopwatch_output()

    def reset_stopwatch(self) -> str:
        """Resets Stopwatch if it has already been started and returns a Stopwatch status string."""
        if self._times["start_time"] is None:
            return self._dialogue["user-reset"]["error-no-stopwatch-available"]

        self._times["start_time"] = None
        self._times["end_time"] = None
        return self._dialogue["user-reset"]["success-reset"]

    def stopwatch_output(self):
        """Returns the final stopwatch time in string form."""
        if self._times["start_time"] is None:
            logging.warning("Stopwatch has not started.")
            return None
        if self._times["end_time"] is None:
            logging.warning("Stopwatch has not ended.")
            return None

        seconds_total = self._times["end_time"] - self._times["start_time"]

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

        stopwatch_output = self._dialogue["program-output"]["stopped-at"].format(time_output)
        return stopwatch_output

    def error(self) -> str:
        """Returns an error string, indicating that Stopwatch is not responding."""
        return self._dialogue["program-error"]["error-not-responding"]

    def generic_response(self) -> str:
        """Returns a generic response for Stopwatch."""
        return self._dialogue["user-generic"]["response"]
