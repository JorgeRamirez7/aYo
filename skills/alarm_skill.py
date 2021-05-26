"""Perform Alarm intents."""
import multiprocessing
import time

from utils.get_time import GetTime
from utils.import_dialogue import ImportDialogue
from utils.readable_time_output import ReadableTimeOutput

class AlarmSkill():
    _dialogue = None

    _alarm_is_running = False
    _alarm_seconds = None
    _alarm_simplified_time = None

    def __init__(self):
        """Imports dialogue for Alarm from a YAML file and stores it in '_dialogue'."""
        self._dialogue = ImportDialogue().initialize_dialogue('alarm')

    def set_alarm(self, user_input:str):
        self._alarm_simplified_time = GetTime().get_clock_time(user_input)

        if not self._alarm_simplified_time:
            return "Sorry, I didn't catch that."
        else:
            self._alarm_is_running = True

            alarm_clock_dict = GetTime().get_clock_time_dict(user_input)
            total_alarm_seconds = GetTime().get_seconds_from_time(alarm_clock_dict

            return "Alarm has been set for {}.".format(self._alarm_simplified_time)

        #return alarm_time
        #readable_time = ReadableTimeOutput().output_clock_time(alarm_time)
        #alarm_time_proper_format = None

        

    def get_current_time(self) -> dict:
        """Gets the current time and stores it in a dictionary of time values."""
        local_time = time.localtime()
        hours_current = time.strftime("%H", local_time)
        minutes_current = time.strftime("%M", local_time)
        seconds_current = time.strftime("%S", local_time)
        
        current_time = {
            "seconds": seconds_current,
            "minutes": minutes_current,
            "hours": hours_current
        }

        return current_time

    def seconds_until_alarm(self, total_alarm_seconds):
        current_time_dict = self.get_current_time()
        total_current_time_seconds = GetTime().get_seconds_from_time(current_time_dict)

        if total_alarm_seconds > total_current_time_seconds:
            return total_alarm_seconds - total_current_time_seconds
        else:
            """If alarm is for next day, figure out how many seconds remain for that day."""
            seconds_until_twelve = 43200 - total_current_time_seconds
            """Add the remaining seconds for the previous day and the alarm seconds to get correct number of alarm seconds."""
            return seconds_until_twelve + total_alarm_seconds


    def alarm_thread(self):
        """Alarm action once the alarm has reached 0 seconds. Notification sound plays and a message is displayed."""
        seconds_left = self._alarm_seconds

        while(seconds_left != 0):
            time.sleep(1)
            if self._timer_is_running == False:
                print("cancelling...")
                break
            seconds_left -= 1

        if self._alarm_is_running:
            """Notify user that timer has been set with sound and text/voice."""
            playsound(self._timer_sfx)
            print(self._dialogue["alarm-has-finished"]["confirmation"].format(self._timer_simplified_time))
            """TODO: Change this from a print statement to calling a function that forces TTS."""
        else:
            print(self._dialogue["cancel-timer"]["confirmation"].format(self._timer_simplified_time))
            self._timer_is_running = False        

    def cancel_alarm(self):
        """Cancels an alarm."""
        """TODO: Implement alarm cancellation."""
        return self._dialogue["cancel-alarm"]["to-be-implemented"]  

    def error(self) -> str:
        """Returns an error string, indicating that Alarm is not responding."""
        return self._dialogue["program-error"]["error-not-responding"]

    def generic_response(self) -> str:
        """Returns a generic response for Alarm."""
        return self._dialogue["user-generic"]["response"]
