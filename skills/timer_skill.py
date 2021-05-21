"""Perform Timer intents."""
from utils.get_time import GetTime
from utils.import_dialogue import ImportDialogue
from utils.readable_time_output import ReadableTimeOutput

class TimerSkill():
    _dialogue = None

    def __init__(self):
        """Imports dialogue for Alarm from a YAML file and stores it in '_dialogue'."""
        self._dialogue = ImportDialogue().initialize_dialogue('timer')

    def set_timer(self, user_input:str):
        user_timer_time = GetTime().get_time(user_input)
        timer_simplified_time = ReadableTimeOutput().output_time(user_timer_time)
        return timer_simplified_time

    def error(self) -> str:
        """Returns an error string, indicating that Timer is not responding."""
        return self._dialogue["program-error"]["error-not-responding"]

    def generic_response(self) -> str:
        """Returns a generic response for Timer."""
        return self._dialogue["user-generic"]["response"]


