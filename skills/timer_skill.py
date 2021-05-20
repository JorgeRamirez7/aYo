"""Perform Timer intents."""
import configparser

from utils.import_dialogue import ImportDialogue

class TimerSkill():
    _dialogue = None

    def __init__(self):
        """Imports dialogue for Alarm from a YAML file and stores it in '_dialogue'."""
        config = configparser.ConfigParser()
        config.read('config/ayo.ini')

        timer_dialogue_file_name = config.get('dialogue', 'timer')
        self._dialogue = ImportDialogue().import_dialogue(timer_dialogue_file_name)




