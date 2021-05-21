"""Search for a Alarm/Timer-related query and perform the desired intent."""
from skills.alarm_skill import AlarmSkill
from skills.timer_skill import TimerSkill
from utils.find_matching_word import FindMatchingWord
from utils.readable_time_output import ReadableTimeOutput

class AlarmTimerIntents():
    def alarm_timer_intent(self, ayo_input:str) -> str:
        alarm_timer_output = None

        if FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["trigger-alarm"]):
            pass
        elif FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["trigger-timer"]):
            timer_time = AlarmSkill().set_alarm(ayo_input)
            alarm_timer_output = ReadableTimeOutput().output_time(timer_time)
        else:
            alarm_timer_output = AlarmSkill().generic_response()

        if alarm_timer_output == None:
            pass
        else:
            return alarm_timer_output
