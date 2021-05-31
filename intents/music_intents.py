"""Search for a Stopwatch-related query and perform the desired intent."""
from skills.music_skills import MusicSkill
from utils.find_matching_word import FindMatchingWord

class MusicIntents(object):
    
    def music_intents(self, user_input):
        key = user_input.split()[0]
        
        if FindMatchingWord().find_match(user_input, FindMatchingWord.query["play"]):
            try:
                argument = user_input.split()[1]
                print(argument)
            except IndexError:
                print("Say play artist <artist>, play podcast <podcast>, or play <song>")
                return

            
            if str(user_input.split()[1]).lower() == 'artist':
                try:
                    word = user_input.split()[2]
                    MusicSkill().play_artist(user_input)
                except IndexError:
                    print("Provide artist")
                
            elif str(user_input.split()[1]).lower() == 'podcast':
                try:
                    word = user_input.split()[2]
                    MusicSkill().play_podcast(user_input)
                except IndexError:
                    print("Provide podcast")

            else:    
                MusicSkill().play_song(user_input)
                

        elif FindMatchingWord().find_match(user_input, FindMatchingWord.query["next"]):
            MusicSkill().next()
        elif FindMatchingWord().find_match(user_input, FindMatchingWord.query["previous"]):
            MusicSkill().previous()
        elif FindMatchingWord().find_match(user_input, FindMatchingWord.query["pause"]):
            MusicSkill().pause()
        elif FindMatchingWord().find_match(user_input, FindMatchingWord.query["resume"]):
            MusicSkill().resume()
        elif FindMatchingWord().find_match(user_input, FindMatchingWord.query["shuffle"]):
            MusicSkill().shuffle()
        