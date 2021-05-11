class ReadableTimeOutput(object):
    def output_time(self, stopwatch_time):
        total_time_in_seconds = int((stopwatch_time["hours"] * 3600) + (stopwatch_time["minutes"] * 60) + stopwatch_time["seconds"])
        minutes, seconds = divmod(total_time_in_seconds, 60)
        hours, minutes = divmod(minutes, 60)

        stopwatch_time_output = {
            "seconds": seconds,
            "minutes": minutes,
            "hours": hours
        }

        seconds_word = ("second" if stopwatch_time_output["seconds"] == 1 else "seconds")
        minutes_word = ("minute" if stopwatch_time_output["minutes"] == 1 else "minutes")
        hours_word = ("hour" if stopwatch_time_output["hours"] == 1 else "hours")
        stopwatch_words = {
            "seconds_word": seconds_word,
            "minutes_word": minutes_word,
            "hours_word": hours_word
        }

        requires_and = False
        time_output = ""

        nonzero_values_remaining = sum(int(number) > 0 for number in stopwatch_time_output.values())
        if nonzero_values_remaining > 1:
            requires_and = True
        
        if stopwatch_time_output["hours"] != 0:
            if requires_and and nonzero_values_remaining == 1:
                time_output += "and "
            time_output += "{0} {1} ".format(stopwatch_time_output["hours"], stopwatch_words["hours_word"])
            if nonzero_values_remaining == 1:
                time_output = time_output.rstrip()
            nonzero_values_remaining -= 1
            
        if stopwatch_time_output["minutes"] != 0:
            if requires_and and nonzero_values_remaining == 1:
                time_output += "and "
            time_output += "{0} {1} ".format(stopwatch_time_output["minutes"], stopwatch_words["minutes_word"])
            if nonzero_values_remaining == 1:
                time_output = time_output.rstrip()
            nonzero_values_remaining -= 1

        if stopwatch_time_output["seconds"] != 0:
            if requires_and and nonzero_values_remaining == 1:
                time_output += "and "
            time_output += "{0} {1} ".format(stopwatch_time_output["seconds"], stopwatch_words["seconds_word"])
            if nonzero_values_remaining == 1:
                time_output = time_output.rstrip()
            nonzero_values_remaining -= 1
            
        return time_output