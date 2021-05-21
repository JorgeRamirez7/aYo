import spotipy
from intents.music_skills import MusicSkill
from spotipy.oauth2 import SpotifyOAuth

class MusicIntents(object):
    if __name__ == '__main__':
	    pass
    
    def music_intents(self, user_input):
        key = user_input.split()[0]
        
        if key == 'Play':
            MusicSkill().play(user_input)
        elif key == 'Next':
            MusicSkill().next()
        elif key == 'Previous':
            MusicSkill().previous()
        elif key == 'Pause':
            MusicSkill().pause()
        elif key == 'Resume':
            MusicSkill().resume()
        elif key == 'Shuffle':
            MusicSkill().shuffle()
        



