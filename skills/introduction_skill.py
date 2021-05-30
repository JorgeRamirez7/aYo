from azure.text_to_speech import TextToSpeech
from skills.random_element_skill import RandomElementSkill
from utils.find_matching_word import FindMatchingWord
from utils.import_dialogue import ImportDialogue

class IntroductionSkill():
    """Introduction/greeting when a user start aYo."""
    introduction_queries = ImportDialogue().import_dialogue("skills/introductions.yaml")
    introduction = RandomElementSkill(introduction_queries["program-response"])

    def ayo_intro(self):
        """Says a random introduction."""
        random_intro = self.introduction.get_random_element()
        TextToSpeech().text_to_speech(random_intro)
        