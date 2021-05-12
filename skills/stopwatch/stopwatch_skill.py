import time
from utils.readable_time_output import ReadableTimeOutput

start_time = None
end_time = None

class StopwatchSkill():
    def start_stopwatch(self):
        global start_time

        if start_time is None:
            start_time = time.time()
            return "Stopwatch has started."
        else:
            return "Stopwatch is already running."

    def stop_stopwatch(self):
        global start_time, end_time

        if start_time is None:
            return "Try starting a stopwatch first."
        else:
            end_time = time.time()
            return self.stopwatch_output()

    def reset_stopwatch(self):
        global start_time, end_time

        if start_time is None:
            return "There is no stopwatch to reset"

        start_time = None
        end_time = None
        return "Stopwatch has been reset"

    def stopwatch_output(self):
        global start_time, end_time

        if start_time is None:
            return "Error. Stopwatch has not started."
        if end_time is None:
            return "Error. Stopwatch has not ended."

        seconds_total = end_time - start_time

        stopwatch_time = {
            "seconds": seconds_total,
            "minutes": 0,
            "hours": 0
        }

        self.reset_stopwatch()
        time_output = ReadableTimeOutput().output_time(stopwatch_time)

        if time_output == None:
            return None

        stopwatch_output = "Stopwatch stopped at {}.".format(time_output)
        return stopwatch_output

    def error(self):
        return "Sorry, Stopwatch is not responding."

    def generic_response(self):
        return "I can create a stopwatch for you. Just say, ayo, start a stopwatch"