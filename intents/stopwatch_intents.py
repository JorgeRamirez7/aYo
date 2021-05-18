from skills.stopwatch_skill import StopwatchSkill
from utils.find_matching_word import FindMatchingWord

class StopwatchIntents():
    def stopwatch_intent(self, ayo_input:str) -> str:
        """Performs an action given a user intent for Stopwatch.
        
            Args:
                ayo_input: The string input from a user, indicating their desired Stopwatch action.

            Returns:
                A Stopwatch-related response string for aYo to speak/display.
        """
        stopwatch_output = None

        if FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["start"]):
            stopwatch_output = StopwatchSkill().start_stopwatch()
        elif FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["stop"]):
            stopwatch_output = StopwatchSkill().stop_stopwatch()
        elif FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["reset"]):
            stopwatch_output = StopwatchSkill().reset_stopwatch()
        else:
            stopwatch_output = StopwatchSkill().generic_response()

        if stopwatch_output == None:
            return StopwatchSkill().error()
        else:
            return stopwatch_output