import multiprocessing
import time

from pathlib import Path
from playsound import playsound

from azure.text_to_speech import TextToSpeech
from utils.get_time import GetTime
from utils.import_dialogue import ImportDialogue
from utils.readable_time_output import ReadableTimeOutput

class AlarmSkill():
    """Perform Alarm intents."""
    _dialogue = ImportDialogue().import_dialogue(Path("skills/alarm.yaml"))
    _alarm_sfx = str(Path("data/alarm.wav"))
    
    _alarm = None
    _alarm_is_running = False
    _alarm_seconds = None
    _alarm_simplified_time = None

    def set_alarm(self, user_input:str):
        """Informs user if alarm was successfully set and calls an alarm process.
            
            Args:
                user_input: The string input from a user, which may include time in the format ##:## AM/PM

            Returns:
                A string confirming that an alarm has been set.
                None if an improper time format was given.
        """
        self._alarm_simplified_time = GetTime().get_clock_time_string(user_input)

        if not self._alarm_simplified_time:
            return self._dialogue["user-set"]["error"]
        else:
            self._alarm_is_running = True

            alarm_clock_dict = GetTime().get_clock_time_dict(user_input)

            """Ex. 2:20 PM = 14 hours and 20 minutes = 51600 seconds."""
            total_alarm_seconds = GetTime().get_seconds_from_time(alarm_clock_dict)

            self._alarm_seconds = self.seconds_until_alarm(total_alarm_seconds)

            self._alarm = multiprocessing.Process(target = self.alarm_process)
            self._alarm.start()

            return self._dialogue["user-set"]["success-set"].format(self._alarm_simplified_time)

    def get_current_time(self) -> dict:
        """Gets the current time and stores it in a dictionary of time values."""
        local_time = time.localtime()
        hours_current = int(time.strftime("%H", local_time))
        minutes_current =int( time.strftime("%M", local_time))
        seconds_current = int(time.strftime("%S", local_time))
        
        current_time = {
            "seconds": seconds_current,
            "minutes": minutes_current,
            "hours": hours_current
        }

        return current_time

    def seconds_until_alarm(self, total_alarm_seconds) -> int:
        """Obtains the number of seconds remaining until the alarm is set off.
            
            Args:
                total_alarm_seconds: The alarm time converted into seconds.

            Returns:
                The total number of seconds remaining until the alarm is set off.
        """
        current_time_dict = self.get_current_time()
        total_current_time_seconds = GetTime().get_seconds_from_time(current_time_dict)

        if total_alarm_seconds > total_current_time_seconds:
            return total_alarm_seconds - total_current_time_seconds
        else:
            """If alarm is for next day, figure out how many seconds remain for that day."""
            """12 hours = 43200 seconds."""
            seconds_until_twelve = 43200 - total_current_time_seconds
            """Add the remaining seconds for the previous day and the alarm seconds to get correct number of alarm seconds."""
            return seconds_until_twelve + total_alarm_seconds

    def alarm_process(self):
        """Alarm action once the alarm has reached 0 seconds. Notification sound plays and a message is displayed."""
        seconds_left = self._alarm_seconds

        while(seconds_left != 0):
            time.sleep(1)
            if self._alarm_is_running == False:
                print("cancelling...")
                break
            seconds_left -= 1

        if self._alarm_is_running:
            """Notify user that timer has been set with sound and text/voice."""
            playsound(self._alarm_sfx)
            self._alarm_is_running = False

            alarm_message = self._dialogue["program-finished"]["confirmation"].format(self._alarm_simplified_time)
            TextToSpeech().text_to_speech(alarm_message)
            
        else:
            print(self._dialogue["user-cancel"]["confirmation"].format(self._timer_simplified_time))
            self._alarm_is_running = False        

    def cancel_alarm(self):
        """Cancels an alarm."""
        """TODO: Implement alarm cancellation."""
        return self._dialogue["user-cancel"]["to-be-implemented"]  

    def error(self) -> str:
        """Returns an error string, indicating that Alarm is not responding."""
        return self._dialogue["program-error"]["error-not-responding"]

    def generic_response(self) -> str:
        """Returns a generic response for Alarm."""
        return self._dialogue["user-generic"]["response"]
