"""Search for a Alarm/Timer-related query and perform the desired intent."""
from skills.alarm_skill import AlarmSkill
from skills.timer_skill import TimerSkill
from utils.find_matching_word import FindMatchingWord

class AlarmTimerIntents():
    def alarm_timer_intent(self, ayo_input:str) -> str:
        alarm_timer_output = None
