"""Import a YAML file into a dictionary."""
import configparser
import logging
import yaml

class ImportDialogue():
    def import_dialogue(self, file_name:str):
        """Imports dialogue from a given YAML file.
        
            Args:
                file_name: The name of the YAML file, including the extension '.YAML'.

            Returns:
                All values in the given file in the form of a dictionary.
                None if the YAML file was not able to be loaded.
        """
        config = configparser.ConfigParser()
        config.read('config/ayo.ini')

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

    def initialize_dialogue(self, dialogue_reference:str):
        """Imports dialogue for a user query from a YAML file.'.
            
            Args:
                dialogue_reference: The reference to a dialogue file name, configured under 'dialogue' in ayo.ini.

            Returns:
                ImportDialogue() object
        """
        config = configparser.ConfigParser()
        config.read('config/ayo.ini')

        dialogue_file_name = config.get('dialogue', dialogue_reference)
        return ImportDialogue().import_dialogue(dialogue_file_name)
