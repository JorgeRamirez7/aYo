from skills.alarm_skill import AlarmSkill
from skills.timer_skill import TimerSkill
from utils.find_matching_word import FindMatchingWord
from utils.import_dialogue import ImportDialogue

class AlarmTimerIntents():
    """Search for a Alarm/Timer-related query and perform the desired intent."""
    alarm_timer_queries = ImportDialogue().import_dialogue("intents/alarm-timer.yaml")
    verb_queries = ImportDialogue().import_dialogue("intents/verbs.yaml")

    def alarm_timer_intent(self, ayo_input:str) -> str:
        alarm_timer_output = None

        if FindMatchingWord().find_match(ayo_input, self.alarm_timer_queries["trigger-alarm"]):
            alarm_timer_output = AlarmSkill().set_alarm(ayo_input)
        
        elif FindMatchingWord().find_match(ayo_input, self.alarm_timer_queries["trigger-timer"]):
            alarm_timer_output = TimerSkill().set_timer(ayo_input)
            
        elif (  FindMatchingWord().find_match(ayo_input, self.verb_queries["stop"]) or 
                FindMatchingWord().find_match(ayo_input, self.verb_queries["reset"])
                ):

            if FindMatchingWord().find_match(ayo_input, self.alarm_timer_queries["timer-only"]):
                alarm_timer_output = TimerSkill().cancel_timer()

            elif FindMatchingWord().find_match(ayo_input, self.alarm_timer_queries["alarm-only"]): 
                alarm_timer_output = AlarmSkill().cancel_alarm()

            else:
                alarm_timer_output = None

        else:

            if FindMatchingWord().find_match(ayo_input, self.alarm_timer_queries["timer-only"]):
                alarm_timer_output = TimerSkill().generic_response()

            elif FindMatchingWord().find_match(ayo_input, self.alarm_timer_queries["alarm-only"]):
                alarm_timer_output = AlarmSkill().generic_response()

            else:
                alarm_timer_output = None

        if alarm_timer_output == None:
            return AlarmSkill().error()

        else:
            return alarm_timer_output
