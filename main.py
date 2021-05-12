from azure.microphone_input import MicrophoneInput
from intents.web_search_intents import WebSearchIntents
import webbrowser

import subprocess
from playsound import playsound
#import run

ayo_result = False

# Example to show voice command for opening webpage as well as searching google
print("Begin speaking...")
user_input = MicrophoneInput().get_voice_input()
if user_input:

    if user_input[-1] == '?' or user_input.split()[0] == "Search":
        ayo_result = WebSearchIntents().web_search_intents(user_input)
    
    # Open popular p/l documentation websites
    # Implement website search in future
    elif user_input.split()[0] == "Open":
        if user_input.split()[1] == "C++.":
            webbrowser.open('http://www.cplusplus.com/')
        elif user_input.split()[1] == "Python.":
            webbrowser.open('https://docs.python.org/3/')
        elif user_input.split()[1] == "Java.":
            webbrowser.open('https://docs.oracle.com/en/java/')
        elif user_input.split()[1] == "terminal.":
            subprocess.run(["C:\\Program Files\\Git\\git-bash.exe"])

    # P/L name as keyword
    # Automatically searches documentation website for following words
    elif user_input.split()[0] == "C++":
        toSearch = str(user_input).replace('.', ' ')
        searchFor = ' '.join(toSearch.split()[1:])
        webbrowser.open('http://www.cplusplus.com/search.do?q={}'.format(searchFor))

    elif user_input.split()[0] == "Python":
        toSearch = str(user_input).replace('.', ' ')
        searchFor = ' '.join(toSearch.split()[1:])
        webbrowser.open('https://docs.python.org/3/search.html?q={}'.format(searchFor))

    elif user_input == "Play music.":
        subprocess.run('python run.py')


# Use hashtable of keywords
# str.split() for first word in a string
# 1. Get first word of string
# 2. Check word against hashtable of keywords, return true or false
# 3. If true send result.text
