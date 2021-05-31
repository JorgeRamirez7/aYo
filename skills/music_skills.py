"""Implementation of Music Intents"""
import configparser
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class MusicSkill():
    device_id = None
    """Creates/Authenticates Spotify object using aYo Spotify Web API developer credentials"""
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config/config.ini')
        client_id = config.get('spotify', 'client_id')
        client_secret = config.get('spotify', 'client_secret')

        self.scope = 'user-modify-playback-state user-read-playback-state playlist-modify-private'
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,client_secret=client_secret,redirect_uri='https://example.com',scope=self.scope))
        try:
            self.device_id = self.sp.devices()['devices'][0]['id']   
        except IndexError:
            print("Spotify not open")
    """
       User must now say Play artist <artist> or Play podcast <podcast> to start playing a specific artist/podcast.
       Without splitting them, if trying to play a specific song e.g. 'Hotel California'
       Spotify will shuffle songs from the band named 'Hotel California'.
    """
    def play_artist(self, to_play):
        to_play = ' '.join(to_play.split()[2:])   
        # track info returned in json form
        track_info = self.sp.search(q=to_play,limit=1,type='artist')

        # if length of track_info is 0, no artist or track found
        if len(track_info['artists']['items']) != 0:
            track_artist_uri = track_info['artists']['items'][0]['uri']
            self.sp.start_playback(device_id=self.device_id,context_uri=track_artist_uri)
        else:
            print("Artist not found")

    def play_podcast(self, to_play):
        to_play = ' '.join(to_play.split()[2:])
        # track info returned in json form
        track_info = self.sp.search(q=to_play,limit=1,type='show')

        # if length of track_info is 0, no artist or track found
        if len(track_info['shows']['items']) != 0:
            track_artist_uri = track_info['shows']['items'][0]['uri']
            self.sp.start_playback(device_id=self.device_id,context_uri=track_artist_uri)
        else:
            print("Podcast not found")

    def play_song(self, to_play):
        to_play = ' '.join(to_play.split()[1:])   
        # track info returned in json form
        track_info = self.sp.search(q=to_play,limit=1,type='track')

        # if length of track_info is 0, no artist or track found
        if len(track_info['tracks']['items']) != 0:
            track_info = self.sp.search(q=to_play,limit=1,type='track')
            track_album_uri = track_info['tracks']['items'][0]['album']['uri'] # needed for context_uri to play specific song
            track_uri = track_info['tracks']['items'][0]['uri']
            self.sp.start_playback(device_id=self.device_id,context_uri=track_album_uri,offset={"uri": track_uri})
        else:
            print("Song not found")

    def next(self):
        self.sp.next_track(device_id=self.device_id)

    def previous(self):
        self.sp.previous_track(device_id=self.device_id)
        
    def pause(self):
        self.sp.pause_playback(device_id=self.device_id)

    def resume(self):
        self.sp.start_playback(device_id=self.device_id)

    def shuffle(self):
        self.sp.shuffle(True, device_id=self.device_id)
    
    def login(self):
        MusicSkill().__init__()
