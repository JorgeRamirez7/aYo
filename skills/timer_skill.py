"""Perform Timer intents."""
import datetime
import multiprocessing
import threading
import time

from utils.get_time import GetTime
from utils.import_dialogue import ImportDialogue
from utils.readable_time_output import ReadableTimeOutput

class TimerSkill():
    _dialogue = None
    _timer_seconds = 0
    _timer_simplified_time = None
    _timer_is_running = False
    _timer = None

    def __init__(self):
        """Imports dialogue for Alarm from a YAML file and stores it in '_dialogue'."""
        self._dialogue = ImportDialogue().initialize_dialogue('timer')

    def set_timer(self, user_input:str):
        user_timer_time = GetTime().get_time(user_input)
        self._timer_seconds = GetTime().get_seconds_from_time(user_timer_time)

        if self._timer_seconds < 5:
            return "Timer must be set for at least 5 seconds."
        else:
            self._timer_is_running = True
            self._timer_simplified_time = ReadableTimeOutput().output_time(user_timer_time)

            self._timer = multiprocessing.Process(target = self.timer_thread)
            self._timer.start()

            return ("Timer set for " + self._timer_simplified_time + ".")

    def cancel_timer(self):
        """Cancels a timer."""
        return "Cancelling timers is currently not supported."

    def error(self) -> str:
        """Returns an error string, indicating that Timer is not responding."""
        return self._dialogue["program-error"]["error-not-responding"]

    def generic_response(self) -> str:
        """Returns a generic response for Timer."""
        return self._dialogue["user-generic"]["response"]

    def timer_thread(self):
        """Timer action once the timer has reached 0 seconds. Notification sound plays and a message is displayed."""
        seconds_left = self._timer_seconds

        while(seconds_left != 0):
            time.sleep(1)
            if self._timer_is_running == False:
                print("cancelling...")
                break
            seconds_left -= 1

        if self._timer_is_running:
            print("RING RING - Your timer for " + self._timer_simplified_time + " has finished.")
            """TODO: Change this from a print statement to calling a function that forces TTS."""
        else:
            print("Timer for " + self._timer_simplified_time + " has been cancelled.")
            self._timer_is_running = False
