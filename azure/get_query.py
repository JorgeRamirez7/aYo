from azure.microphone_input import MicrophoneInput
from azure.text_to_speech import TextToSpeech
from intents.intents import Intents

class GetQuery():
    def query(self):
        """Gets the query from a user input via text or speech and outputs it via text and/or speech."""
        microphone_input = True
        text_to_speech = True


       # ayo_is_running = True

        #while ayo_is_running:
        print("Begin speaking...")

        if microphone_input:
            user_input = MicrophoneInput().get_voice_input()
        else:
            user_input = input()

        if user_input:
            ayo_result = Intents().intents(user_input)
            if ayo_result is not None and user_input != "":
                if text_to_speech:
                    TextToSpeech().text_to_speech(ayo_result)
                else:
                    print(ayo_result)
        #ayo_is_running = False
        print()
