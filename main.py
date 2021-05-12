from azure.microphone_input import MicrophoneInput
from intents.web_search_intents import WebSearchIntents
from intents.open_documentation_intents import OpenDocumentationIntents
from intents.search_documentation_intents import SearchDocumentationIntents
from intents.music_intents import MusicIntents

ayo_result = False

# Example to show voice command for opening webpage as well as searching google
print("Begin speaking...")
user_input = MicrophoneInput().get_voice_input()
if user_input:

    if user_input[-1] == '?' or user_input.split()[0] == "Search":
        ayo_result = WebSearchIntents().web_search_intents(user_input)
    
    elif user_input.split()[0] == "Open":
        ayo_result = OpenDocumentationIntents().open_documentation_intents(user_input)

    elif user_input.split()[0] == "C++" or user_input.split()[0] == "Python":
        ayo_result = SearchDocumentationIntents().search_documentation_intents(user_input)

    elif user_input == "Play music.":
        ayo_result = MusicIntents().music_intents(user_input)


# Use hashtable of keywords
# str.split() for first word in a string
# 1. Get first word of string
# 2. Check word against hashtable of keywords, return true or false
# 3. If true send result.text
