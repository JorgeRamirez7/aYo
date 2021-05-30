from skills.music_skills import MusicSkill
from utils.find_matching_word import FindMatchingWord
from utils.import_dialogue import ImportDialogue

class MusicIntents(object):
    """Search for a Stopwatch-related query and perform the desired intent."""
    music_queries = ImportDialogue().import_dialogue("intents/music.yaml")

    def music_intents(self, user_input):
        key = user_input.split()[0]
        
        if FindMatchingWord().find_match(user_input, self.music_queries["play"]):
            if str(user_input.split()[1]).lower() == 'artist':
                MusicSkill().play_artist(user_input)
            elif str(user_input.split()[1]).lower() == 'podcast':
                MusicSkill().play_podcast(user_input)
            else:
                MusicSkill().play_song(user_input)
        elif FindMatchingWord().find_match(user_input, self.music_queries["next"]):
            MusicSkill().next()
        elif FindMatchingWord().find_match(user_input, self.music_queries["previous"]):
            MusicSkill().previous()
        elif FindMatchingWord().find_match(user_input, self.music_queries["pause"]):
            MusicSkill().pause()
        elif FindMatchingWord().find_match(user_input, self.music_queries["resume"]):
            MusicSkill().resume()
        elif FindMatchingWord().find_match(user_input, self.music_queries["shuffle"]):
            MusicSkill().shuffle()
        