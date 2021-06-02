from azure.ayo_keyword import AyoKeyword
from azure.microphone_input import MicrophoneInput
from azure.text_to_speech import TextToSpeech
from intents.intents import Intents

from pathlib import Path
from playsound import playsound
import configparser
import multiprocessing

class GetQuery():
    _sfx_ayo_activated = str(Path("data/ayo_keyword/activated.mp3"))
    _sfx_ayo_success = str(Path("data/ayo_keyword/success.mp3"))
    _sfx_ayo_failed = str(Path("data/ayo_keyword/failed.mp3"))

    ayo_config = configparser.ConfigParser()
    ayo_config.read(Path("config/ayo.ini"))

    keyword_mode = ayo_config.getboolean('ayo_input', 'keyword_mode')
    work_mode = ayo_config.getboolean('ayo_input', 'work_mode')
    text_to_speech = ayo_config.getboolean('general', 'speech')
    
    def query(self):
        """Gets the query from a user input via text or speech and outputs it via text and/or speech."""

        # Voice Keyword Mode. Listens for an aYo keyword before processing voice input.
        ayo_keyword = self.keyword_mode

        # Work Mode. Listens for voice input automatically.
        microphone_input = self.work_mode

        text_to_speech = self.text_to_speech

        if ayo_keyword:
            AyoKeyword().ayo_keyword()
            _sfx_activated = multiprocessing.Process(target = GetQuery().ayo_activated)
            _sfx_activated.start()
            user_input = MicrophoneInput().get_voice_input()

        elif microphone_input:
            print("Begin speaking...")
            user_input = MicrophoneInput().get_voice_input()

        else:
            print("Begin typing...")
            user_input = input()

        if user_input:
            ayo_result = Intents().intents(user_input)
            if ayo_result is not None and user_input != "":
                if text_to_speech:
                    if ayo_keyword:
                        playsound(GetQuery()._sfx_ayo_success)
                    TextToSpeech().text_to_speech(ayo_result)
                else:
                    print(ayo_result)
                    
        else:
            if ayo_keyword:
                playsound(GetQuery()._sfx_ayo_failed)

        print()

    def ayo_activated(self):
        playsound(self._sfx_ayo_activated)
