from pathlib import Path
from playsound import playsound

from azure.text_to_speech import TextToSpeech
from skills.random_element_skill import RandomElementSkill
from utils.find_matching_word import FindMatchingWord
from utils.import_dialogue import ImportDialogue

class IntroductionSkill():
    """Introduction/greeting when a user start aYo."""
    _intro_sfx = 'data/intro.wav'
    introduction_queries = ImportDialogue().import_dialogue(Path("skills/introductions.yaml"))
    introduction = RandomElementSkill(introduction_queries["program-response"])

    def ayo_intro(self):
        """Plays sfx and says a random introduction."""
        playsound(self._intro_sfx)
        random_intro = self.introduction.get_random_element()
        TextToSpeech().text_to_speech(random_intro)
        