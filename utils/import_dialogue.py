from pathlib import Path

import configparser
import logging
import yaml

class ImportDialogue():
    """Import a YAML file into a dictionary."""

    try:
        config = configparser.ConfigParser()
        config.read(Path('config/ayo.ini'))

        ayo_localization = config.get('general', 'localization')
        folder_directory = config.get('dialogue', 'directory')

    except:
        logging.critical("Could not load 'general' or 'dialogue' from ayo.ini - aYo cannot function without these.")

    def import_dialogue(self, file_name:str):
        """Imports dialogue from a given YAML file.
        
            Args:
                file_name: The name of the YAML file, including the extension '.YAML'.
            Returns:
                All values in the given file in the form of a dictionary.
                None if the YAML file was not able to be loaded.
        """
        file_directory = Path("dialogue/en_US/{}".format(file_name))

        try:
            with open(file_directory) as file:
                dialogue = yaml.load(file, Loader=yaml.FullLoader)
            return dialogue

        except:
            logging.warning("Could not load dialogue located in {0}".format(file_directory))
            return None
