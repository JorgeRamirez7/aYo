from azure.microphone_input import MicrophoneInput
from intents.intents import Intents

def main():
    DEBUG_TEXT_MODE = False
    ayo_is_running = True

    while ayo_is_running:
        print("Begin speaking...")
        
        if DEBUG_TEXT_MODE:
            user_input = input()
        else:
            user_input = MicrophoneInput().get_voice_input()

        if user_input:
            ayo_result = Intents().intents(user_input)
            if ayo_result is not None and user_input != "":
                print(ayo_result)

        print()

if __name__ == "__main__":
    main()

# Use hashtable of keywords
# str.split() for first word in a string
# 1. Get first word of string
# 2. Check word against hashtable of keywords, return true or false
# 3. If true send result.text
