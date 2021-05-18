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
        STOPWATCH_DIALOGUE_FILE_NAME = "stopwatch.yaml"
        StopwatchSkill._dialogue = ImportDialogue().import_dialogue(STOPWATCH_DIALOGUE_FILE_NAME)

    def start_stopwatch(self) -> str:
        """Starts Stopwatch by storing the current time and returns a Stopwatch status string."""
        if StopwatchSkill._times["start_time"] is None:
            StopwatchSkill._times["start_time"] = time.time()
            return StopwatchSkill._dialogue["user-start"]["success-started"]
        else:
            return StopwatchSkill._dialogue["user-start"]["error-already-running"]

    def stop_stopwatch(self) -> str:
        """Stops Stopwatch by storing the current time and returns a stopwatch time string."""
        if StopwatchSkill._times["start_time"] is None:
            return StopwatchSkill._dialogue["user-stop"]["error-hasnt-been-started"]
        else:
            StopwatchSkill._times["end_time"] = time.time()
            return self.stopwatch_output()

    def reset_stopwatch(self) -> str:
        """Resets Stopwatch if it has already been started and returns a Stopwatch status string."""
        if StopwatchSkill._times["start_time"] is None:
            return StopwatchSkill._dialogue["user-reset"]["error-no-stopwatch-available"]

        StopwatchSkill._times["start_time"] = None
        StopwatchSkill._times["end_time"] = None
        return StopwatchSkill._dialogue["user-reset"]["success-reset"]

    def stopwatch_output(self):
        """Returns the final stopwatch time in string form."""
        if StopwatchSkill._times["start_time"] is None:
            logging.warning("Stopwatch has not started.")
            return None
        if StopwatchSkill._times["end_time"] is None:
            logging.warning("Stopwatch has not ended.")
            return None

        seconds_total = StopwatchSkill._times["end_time"] - StopwatchSkill._times["start_time"]

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

        stopwatch_output = StopwatchSkill._dialogue["program-output"]["stopped-at"].format(time_output)
        return stopwatch_output

    def error(self) -> str:
        """Returns an error string, indicating that Stopwatch is not responding."""
        return StopwatchSkill._dialogue["program-error"]["error-not-responding"]

    def generic_response(self) -> str:
        """Returns a generic response for Stopwatch."""
        return StopwatchSkill._dialogue["user-generic"]["response"]
