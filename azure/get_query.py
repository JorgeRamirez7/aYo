from azure.ayo_keyword import AyoKeyword
from azure.microphone_input import MicrophoneInput
from azure.text_to_speech import TextToSpeech
from intents.intents import Intents

class GetQuery():
    def get_query(self):
        """Gets the query from a user input via text or speech and outputs it via text and/or speech."""
        ayo_keyword = True
        microphone_input = True
        text_to_speech = True

        ayo_is_running = True

        while ayo_is_running:

            if ayo_keyword:
                AyoKeyword().ayo_keyword()
                print("Start speaking")
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
                        TextToSpeech().text_to_speech(ayo_result)
                    else:
                        print(ayo_result)

            print()
