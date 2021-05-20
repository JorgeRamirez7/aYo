"""Perform Timer intents."""
from utils.import_dialogue import ImportDialogue

class TimerSkill():
    _dialogue = None

    def __init__(self):
        """Imports dialogue for Alarm from a YAML file and stores it in '_dialogue'."""
        self._dialogue = ImportDialogue().initialize_dialogue('timer')

    def generic_response(self) -> str:
        """Returns a generic response for Timer."""
        return self._dialogue["user-generic"]["response"]


