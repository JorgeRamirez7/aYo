from azure.microphone_input import MicrophoneInput
from azure.text_to_speech import TextToSpeech
from intents.intents import Intents
from skills.introduction_skill import IntroductionSkill

ayo_is_running = True
ayo_introduction = True

microphone_input = True
text_to_speech = True

def main():
    global ayo_is_running, introduction, microphone_input, text_to_speech

    while ayo_is_running:
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

        print()

if __name__ == "__main__":
    if ayo_introduction:
        IntroductionSkill().ayo_intro()

    main()
