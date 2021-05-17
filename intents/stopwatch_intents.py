from skills.stopwatch_skill import StopwatchSkill
from utils.find_matching_word import FindMatchingWord

class StopwatchIntents():
    def stopwatch_intent(self, ayo_input):
        stopwatch_output = None

        if FindMatchingWord().find_match(ayo_input, FindMatchingWord.words_for_start):
            stopwatch_output = StopwatchSkill().start_stopwatch()
        elif FindMatchingWord().find_match(ayo_input, FindMatchingWord.words_for_stop):
            stopwatch_output = StopwatchSkill().stop_stopwatch()
        elif FindMatchingWord().find_match(ayo_input, FindMatchingWord.words_for_reset):
            stopwatch_output = StopwatchSkill().reset_stopwatch()
        else:
            stopwatch_output = StopwatchSkill().generic_response()

        if stopwatch_output == None:
            return StopwatchSkill().error()
        else:
            return stopwatch_output