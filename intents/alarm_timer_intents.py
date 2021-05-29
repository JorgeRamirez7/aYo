from skills.alarm_skill import AlarmSkill
from skills.timer_skill import TimerSkill
from utils.find_matching_word import FindMatchingWord

class AlarmTimerIntents():
    """Search for a Alarm/Timer-related query and perform the desired intent."""

    def alarm_timer_intent(self, ayo_input:str) -> str:
        alarm_timer_output = None

        if FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["trigger-alarm"]):
            alarm_timer_output = AlarmSkill().set_alarm(ayo_input)
        
        elif FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["trigger-timer"]):
            alarm_timer_output = TimerSkill().set_timer(ayo_input)
            
        elif (  FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["stop"]) or 
                FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["reset"])
                ):

            if FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["timer-only"]):
                alarm_timer_output = TimerSkill().cancel_timer()

            elif FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["alarm-only"]): 
                alarm_timer_output = AlarmSkill().cancel_alarm()

            else:
                alarm_timer_output = None

        else:

            if FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["timer-only"]):
                alarm_timer_output = TimerSkill().generic_response()

            elif FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["alarm-only"]):
                alarm_timer_output = AlarmSkill().generic_response()

            else:
                alarm_timer_output = None

        if alarm_timer_output == None:
            return AlarmSkill().error()

        else:
            return alarm_timer_output
