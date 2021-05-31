import datetime
import multiprocessing
import time

from pathlib import Path
from playsound import playsound

from azure.text_to_speech import TextToSpeech
from utils.get_time import GetTime
from utils.import_dialogue import ImportDialogue
from utils.readable_time_output import ReadableTimeOutput

class TimerSkill():
    """Perform Timer intents."""
    _dialogue = ImportDialogue().import_dialogue(Path("skills/timer.yaml"))
    _timer_sfx = str(Path("data/alarm.wav"))

    _timer = None
    _timer_is_running = False
    _timer_seconds = 0
    _timer_simplified_time = None
    
    def set_timer(self, user_input:str):
        """Informs user if timer was successfully set and calls a timer process.
            
            Args:
                user_input: The string input from a user, which may include time in the format "# minutes and # seconds".

            Returns:
                A string confirming that a timer has been set.
                A string telling the user that the timer has been set for less than 5 seconds.
        """
        user_timer_time = GetTime().get_time(user_input)
        if (user_timer_time is None):
            return self._dialogue["user-set"]["error-not-number"]

        self._timer_seconds = GetTime().get_seconds_from_time(user_timer_time)

        if self._timer_seconds < 5:
            return self._dialogue["user-set"]["error-not-at-least-5-seconds"]
        else:
            self._timer_is_running = True
            self._timer_simplified_time = ReadableTimeOutput().output_time(user_timer_time)

            self._timer = multiprocessing.Process(target = self.timer_process)
            self._timer.start()

            return self._dialogue["user-set"]["success-set"].format(self._timer_simplified_time)

    def timer_process(self):
        """Timer action once the timer has reached 0 seconds. Notification sound plays and a message is displayed."""
        seconds_left = self._timer_seconds

        while(seconds_left != 0):
            time.sleep(1)
            if self._timer_is_running == False:
                print("cancelling...")
                break
            seconds_left -= 1

        if self._timer_is_running:
            """Notify user that timer has been set with sound and text/voice."""
            playsound(self._timer_sfx)
            self._timer_is_running = False

            timer_message = self._dialogue["program-has-finished"]["confirmation"].format(self._timer_simplified_time)
            TextToSpeech().text_to_speech(timer_message)

        else:
            print(self._dialogue["user-cancel"]["success-confirmation"].format(self._timer_simplified_time))
            self._timer_is_running = False

    def cancel_timer(self):
        """Cancels a timer."""
        """TODO: Implement timer cancellation."""
        return self._dialogue["user-cancel"]["to-be-implemented"]  

    def error(self) -> str:
        """Returns an error string, indicating that Timer is not responding."""
        return self._dialogue["program-error"]["error-not-responding"]

    def generic_response(self) -> str:
        """Returns a generic response for Timer."""
        return self._dialogue["user-generic"]["response"]
