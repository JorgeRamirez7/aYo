from azure.microphone_input import MicrophoneInput
from azure.text_to_speech import TextToSpeech
from intents.intents import Intents

from ui.ui_classes.ayo_login import AyoLogin
from PyQt5 import QtWidgets

def main():
    MICROPHONE_INPUT = True
    TEXT_TO_SPEECH = True

    ayo_is_running = True

    while ayo_is_running:
        print("Begin speaking...")

        if MICROPHONE_INPUT:
            user_input = MicrophoneInput().get_voice_input()
        else:
            user_input = input()

        if user_input:
            ayo_result = Intents().intents(user_input)
            if ayo_result is not None and user_input != "":
                if TEXT_TO_SPEECH:
                    TextToSpeech().text_to_speech(ayo_result)
                else:
                    print(ayo_result)

        print()

if __name__ == "__main__":


#If this is giving you an error add "python.analysis.extraPaths": ["./UI"] to your settings.json file
    app = QtWidgets.QApplication([])
    win = AyoLogin()
    win.show()
    app.exec()

    main()

# Use hashtable of keywords
# str.split() for first word in a string
# 1. Get first word of string
# 2. Check word against hashtable of keywords, return true or false
# 3. If true send result.text
