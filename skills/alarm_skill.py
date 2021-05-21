"""Perform Alarm intents."""
from utils.get_time import GetTime
from utils.import_dialogue import ImportDialogue

class AlarmSkill():
    _dialogue = None

    def __init__(self):
        """Imports dialogue for Alarm from a YAML file and stores it in '_dialogue'."""
        self._dialogue = ImportDialogue().initialize_dialogue('alarm')

    def set_alarm(self, user_input:str):
        time = GetTime().get_time(user_input)
        return time

    def generic_response(self) -> str:
        """Returns a generic response for Alarm."""
        return self._dialogue["user-generic"]["response"]


