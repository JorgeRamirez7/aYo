"""Search for a Alarm/Timer-related query and perform the desired intent."""
from skills.alarm_skill import AlarmSkill
from skills.timer_skill import TimerSkill
from utils.find_matching_word import FindMatchingWord

class AlarmTimerIntents():
    def alarm_timer_intent(self, ayo_input:str) -> str:
        alarm_timer_output = None

        if FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["trigger-alarm"]):
            alarm_timer_output = AlarmSkill().set_alarm(ayo_input)
        
        elif FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["trigger-timer"]):
            
            if FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["start"]):
                alarm_timer_output = TimerSkill().set_timer(ayo_input)
            
        elif (  FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["stop"]) or 
                FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["reset"])
                ):
            if FindMatchingWord().find_match(ayo_input, FindMatchingWord.query["timer-only"]):
                alarm_timer_output = TimerSkill().cancel_timer()
        
            else: 
                alarm_timer_output = AlarmSkill().generic_response()

        else:
            alarm_timer_output = AlarmSkill().generic_response()

        if alarm_timer_output == None:
            return AlarmSkill().error()
        else:
            return alarm_timer_output
