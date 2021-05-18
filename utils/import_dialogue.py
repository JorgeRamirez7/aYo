import logging
import yaml

AYO_LOCALIZATION = "en_US"
FOLDER_DIRECTORY = "dialogue"

class ImportDialogue(object):
    def import_dialogue(self, file_name):
        file_directory = "{0}\{1}\{2}".format(FOLDER_DIRECTORY, AYO_LOCALIZATION, file_name)

        try:
            with open(file_directory) as file:
                dialogue = yaml.load(file, Loader=yaml.FullLoader)
            return dialogue

        except:
            logging.warning("Could not load dialogue located in {0}".format(file_directory))
            return None
