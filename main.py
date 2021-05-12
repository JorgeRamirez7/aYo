from azure.microphone_input import MicrophoneInput
from intents.intents import Intents

ayo_result = False

# Example to show voice command for opening webpage as well as searching google
print("Begin speaking...")
user_input = MicrophoneInput().get_voice_input()

if user_input:
    ayo_result = Intents().intents(user_input)

# Use hashtable of keywords
# str.split() for first word in a string
# 1. Get first word of string
# 2. Check word against hashtable of keywords, return true or false
# 3. If true send result.text
