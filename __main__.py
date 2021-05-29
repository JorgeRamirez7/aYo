from azure.microphone_input import MicrophoneInput
from azure.text_to_speech import TextToSpeech
from intents.intents import Intents

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
    main()
