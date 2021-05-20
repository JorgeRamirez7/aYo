"""Perform Alarm intents."""
import configparser

from utils.import_dialogue import ImportDialogue

class AlarmSkill():
    _dialogue = None

    def __init__(self):
        """Imports dialogue for Alarm from a YAML file and stores it in '_dialogue'."""
        config = configparser.ConfigParser()
        config.read('config/ayo.ini')

        alarm_dialogue_file_name = config.get('dialogue', 'alarm')
        self._dialogue = ImportDialogue().import_dialogue(alarm_dialogue_file_name)




