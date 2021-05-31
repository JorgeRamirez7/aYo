from pathlib import Path

from skills.music_skills import MusicSkill
from utils.find_matching_word import FindMatchingWord
from utils.import_dialogue import ImportDialogue

class MusicIntents(object):
    """Search for a Stopwatch-related query and perform the desired intent."""
    music_queries = ImportDialogue().import_dialogue(Path("intents/music.yaml"))

    def music_intents(self, user_input:str):
        if FindMatchingWord().find_match(user_input, self.music_queries["play"]):
            # These just try to assign the song/artist/podcast to an unused variable to check for an index error
            # I'm sure there's cleaner way, but this works
            try:
                argument = user_input.split()[1]
            except IndexError:
                print("Say play <song>, play artist <artist>, or play podcast <podcast>")
                return
            if str(user_input.split()[1]).lower() == 'artist':
                try:
                    argument = user_input.split()[2]
                    MusicSkill().play_artist(user_input)
                except IndexError:
                    print("Provide an artist")
                    return    
            elif str(user_input.split()[1]).lower() == 'podcast':
                try:
                    argument = user_input.split()[2]
                    MusicSkill().play_podcast(user_input)
                except IndexError:
                    print("Provide a podcast")
                    return
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
        