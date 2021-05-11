from skills.stopwatch.stopwatch_skill import StopwatchSkill
from utils.find_matching_word import FindMatchingWord

class StopwatchIntent():
    def stopwatch_intent(self, ayo_input):
        if FindMatchingWord().find_match(ayo_input, FindMatchingWord.words_for_start):
            return StopwatchSkill().start_stopwatch()
        elif FindMatchingWord().find_match(ayo_input, FindMatchingWord.words_for_stop):
            return StopwatchSkill().stop_stopwatch()
        elif FindMatchingWord().find_match(ayo_input, FindMatchingWord.words_for_reset):
            return StopwatchSkill().reset_stopwatch()
        else:
            return "I can create a stopwatch for you. Just say, ayo, start a stopwatch"