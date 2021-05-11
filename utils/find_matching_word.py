import re

class FindMatchingWord(object):
    words_for_start = ['start', 'begin', 'initiate', 'commence', 'set']
    words_for_stop = ['end', 'stop ', 'terminate', 'finish', 'halt', 'conclude', 'close']
    words_for_reset = ['reset', 'cancel']

    words_for_stopwatch = ['stopwatch']
    words_for_timer = ['timer', 'alarm']

    def find_match(self, input, words_list):
        for word in words_list:
            match_found = re.search(r"\b{}\b".format(word), input, re.IGNORECASE)
            if match_found:
                return True
        return False
