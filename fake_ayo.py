from intents.stopwatch_intent import StopwatchIntent
from utils.find_matching_word import FindMatchingWord

if __name__ == "__main__":
    ayo_is_running = True
    is_blank_response = False

    while ayo_is_running:
        if not is_blank_response:
            print("What should I do?")
        is_blank_response = False

        ayo_input = input()

        if FindMatchingWord().find_match(ayo_input, FindMatchingWord().words_for_stopwatch):
            print(StopwatchIntent().stopwatch_intent(ayo_input))
        elif FindMatchingWord().find_match(ayo_input, FindMatchingWord().words_for_timer):
            print("timer stuff")
        elif ayo_input == "":
            print("...")
            is_blank_response = True
        else:
            print("You asked for something other than a stopwatch or a timer")
        print()