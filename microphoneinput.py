import azure.cognitiveservices.speech as speechsdk
import webbrowser

import subprocess
from playsound import playsound
import run
import time

speech_key, service_region = "94aa9a2d1bb142e2a5e82d0f4c7d999a", "westus2"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

stopwatch_is_on = False



print("Begin speaking...")

result = speech_recognizer.recognize_once()

# Example to show voice command for opening webpage as well as searching google
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    resultText = str(result.text).replace('.', ' ')


    print("Recognized: {}".format(result.text))

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

    elif result.text == "Start stopwatch.":
        if stopwatch_is_on:
            print("Stopwatch is already running")
        else:
            start_time = time.time()
            stopwatch_is_on = True
            print("Stopwatch has started")

    elif result.text == "Stop stopwatch.":
        if not stopwatch_is_on:
            print("Stopwatch is not currently running")
        else:
            end_time = time.time()
            seconds_total = end_time - start_time
            stopwatch_output(seconds_total)
            stopwatch_is_on = False


elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))

elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))

def stopwatch_output(seconds_elapsed):
    minutes = int(seconds_elapsed // 60)
    seconds = int(seconds_elapsed % 60)
    hours = int(minutes // 60)
    stopwatch_stop_text = "Stopwatch stopped at"

    if int(seconds) == 1:
        seconds_word = "second"
    else:
        seconds_word = "seconds"

    if int(minutes) == 1:
        minutes_word = "minute"
    else:
        minutes_word = "minutes"

    if int(hours) == 1:
        hours_word = "hour"
    else:
        hours_word = "hours"

    if hours == 0 and minutes == 0:
        print("{0} {1} {2}".format(stopwatch_stop_text, seconds, seconds_word))
    elif hours == 0:
        if seconds == 0:
            print("{0} {1} {2}".format(stopwatch_stop_text, minutes, minutes_word))
        else:
            print("{0} {1} {2} and {3} {4}".format(stopwatch_stop_text, minutes, minutes_word, seconds, seconds_word))
    else:
        if minutes == 0:
            if seconds == 0:
                print("{0} {1} {2}".format(stopwatch_stop_text, hours, hours_word))
            else:
                print("{0} {1} {2} and {3} {4}".format(stopwatch_stop_text, hours, hours_word, seconds, seconds_word))
        else:
            if seconds == 0:
                print("{0} {1} {2} and {3} {4}".format(stopwatch_stop_text, hours, hours_word, minutes, minutes_word))
            else:
                print("{0} {1} {2} {3} {4} and {5} {6}".format(stopwatch_stop_text, hours, hours_word, minutes, minutes_word, seconds, seconds_word))


# Use hashtable of keywords
# str.split() for first word in a string
# 1. Get first word of string
# 2. Check word against hashtable of keywords, return true or false
# 3. If true send result.text
