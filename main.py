from azure.microphone_input import microphone_input
import webbrowser

import subprocess
from playsound import playsound
import run

# Example to show voice command for opening webpage as well as searching google
print("Begin speaking...")
user_input = microphone_input().get_voice_input()
if user_input:

    # Send result.text through google search in last char is a '?'
    if result.text[-1] == '?':
        webbrowser.open('https://www.google.com/search?q={}'.format(result.text))

    # Search keyword function
    # Search google ignoring first word
    elif result.text.split()[0] == "Search":
        searchFor = ' '.join(result.text.split()[1:])
        webbrowser.open('https://www.google.com/search?q={}'.format(searchFor))
        
    
    # Open popular p/l documentation websites
    # Implement website search in future
    elif result.text.split()[0] == "Open":
        if result.text.split()[1] == "C++.":
            webbrowser.open('http://www.cplusplus.com/')
        elif result.text.split()[1] == "Python.":
            webbrowser.open('https://docs.python.org/3/')
        elif result.text.split()[1] == "Java.":
            webbrowser.open('https://docs.oracle.com/en/java/')
        elif result.text.split()[1] == "terminal.":
            subprocess.run(["C:\\Program Files\\Git\\git-bash.exe"])

    # P/L name as keyword
    # Automatically searches documentation website for following words
    elif result.text.split()[0] == "C++":
        toSearch = str(result.text).replace('.', ' ')
        searchFor = ' '.join(toSearch.split()[1:])
        webbrowser.open('http://www.cplusplus.com/search.do?q={}'.format(searchFor))

    elif result.text.split()[0] == "Python":
        toSearch = str(result.text).replace('.', ' ')
        searchFor = ' '.join(toSearch.split()[1:])
        webbrowser.open('https://docs.python.org/3/search.html?q={}'.format(searchFor))

    elif result.text == "Play music.":
        subprocess.run('python run.py')


# Use hashtable of keywords
# str.split() for first word in a string
# 1. Get first word of string
# 2. Check word against hashtable of keywords, return true or false
# 3. If true send result.text
