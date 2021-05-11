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

        if stopwatch_time_output["hours"] == 0 and stopwatch_time_output["minutes"] == 0:
            return self.output_between_0_and_59_seconds(stopwatch_time_output, stopwatch_words)

        elif stopwatch_time_output["hours"] == 0:
            return self.output_between_1_and_59_minutes(stopwatch_time_output, stopwatch_words)

        else:
            return self.output_is_1_hour_or_more(stopwatch_time_output, stopwatch_words)

    def output_between_0_and_59_seconds(self, sw_time, sw_words):
        return "{0} {1}".format(
            sw_time["seconds"], 
            sw_words["seconds_word"])

    def output_between_1_and_59_minutes(self, sw_time, sw_words):
        if sw_time["seconds"] == 0:
            return "{0} {1}".format(
                sw_time["minutes"], 
                sw_words["minutes_word"])
        else:
            return "{0} {1} and {2} {3}".format(
                sw_time["minutes"], 
                sw_words["minutes_word"], 
                sw_time["seconds"], 
                sw_words["seconds_word"])

    def output_is_1_hour_or_more(self, sw_time, sw_words):
        if sw_time["minutes"] == 0:
            if sw_time["seconds"] == 0:
                return "{0} {1}".format(
                    sw_time["hours"], 
                    sw_words["hours_word"])
            else:
                return "{0} {1} and {2} {3}".format(
                    sw_time["hours"], 
                    sw_words["hours_word"], 
                    sw_time["seconds"], 
                    sw_words["seconds_word"])
        else:
            if sw_time["seconds"] == 0:
                return "{0} {1} and {2} {3}".format(
                    sw_time["hours"], 
                    sw_words["hours_word"], 
                    sw_time["minutes"], 
                    sw_words["minutes_word"])
            elif sw_time["seconds"] > 0:
                return "{0} {1} {2} {3} and {4} {5}".format(
                    sw_time["hours"], 
                    sw_words["hours_word"], 
                    sw_time["minutes"], 
                    sw_words["minutes_word"], 
                    sw_time["seconds"], 
                    sw_words["seconds_word"])
            else:
                return "Output Error. Time is not valid."