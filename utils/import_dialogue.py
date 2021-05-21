"""Import a YAML file into a dictionary."""
import configparser
import logging
import yaml

class ImportDialogue():
    def initialize_dialogue(self, dialogue_reference:str):
        """Imports dialogue for a user query from a YAML file.'.
            
            Args:
                dialogue_reference: The reference to a dialogue file name, configured under 'dialogue' in ayo.ini.

            Returns:
                All values in the given file in the form of a dictionary.
                None if the YAML file was not able to be loaded.
        """
        config = configparser.ConfigParser()
        config.read('config/ayo.ini')

        file_name = config.get('dialogue', dialogue_reference)

        ayo_localization = config.get('general', 'localization')
        folder_directory = config.get('dialogue', 'directory')

        file_directory = "{0}{1}\{2}".format(folder_directory, ayo_localization, file_name)

        try:
            with open(file_directory) as file:
                dialogue = yaml.load(file, Loader=yaml.FullLoader)
            return dialogue

        except:
            logging.warning("Could not load dialogue located in {0}".format(file_directory))
            return None
