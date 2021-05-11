import re
from timerstopwatchtest import AyoStopwatch
from ayotimer import AyoTimer

words_for_start = ['start', 'begin', 'initiate', 'commence', 'set']
words_for_stop = ['end', 'stop ', 'terminate', 'finish', 'halt', 'conclude', 'close']
words_for_reset = ['reset', 'cancel']

words_for_stopwatch = ['stopwatch']
words_for_timer = ['timer', 'alarm']

def ayo_stopwatch(ayo_input):
    if found_match(ayo_input, words_for_start):
        return AyoStopwatch().start_stopwatch()
    elif found_match(ayo_input, words_for_stop):
        return AyoStopwatch().stop_stopwatch()
    elif found_match(ayo_input, words_for_reset):
        return AyoStopwatch().reset_stopwatch()
    else:
        return "I can create a stopwatch for you. Just say, ayo, start a stopwatch"

def ayo_timer(ayo_input):
    return "timer stuff"

def ayo_generic(ayo_input):
    return "You asked for something other than a stopwatch or a timer"

def found_match(input, words_list):
    for word in words_list:
        match_found = re.search(r"\b{}\b".format(word), input)
        if match_found:
            return True
    return False

if __name__ == "__main__":
    ayo_is_running = True

    while ayo_is_running:
        print("What should I do?")
        ayo_input = input()
        if found_match(ayo_input, words_for_stopwatch):
            print(ayo_stopwatch(ayo_input))
        elif found_match(ayo_input, words_for_timer):
            print(ayo_timer(ayo_input))
        elif ayo_input == "":
            print("...")
        else:
            print(ayo_generic(ayo_input))
        print()