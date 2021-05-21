import configparser
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class MusicSkill():
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

    def play(self, to_play):
        to_play = ' '.join(to_play.split()[1:])   
        # track info returned in json form
        track_info = self.sp.search(q=to_play,limit=1,type='track')

        # if length of track_info is 0, no artist or track found
        if len(track_info['tracks']['items']) != 0:
            track_artist = track_info['tracks']['items'][0]['album']['artists'][0]['name']
            # if the artist name is equal to to_play argument, shuffle artist songs
            if track_artist == to_play:
                track_artist_uri = track_info['artists']['items'][0]['uri']
                self.sp.start_playback(device_id=self.device_id,context_uri=track_artist_uri)
            # play specific track
            else:
                track_info = self.sp.search(q=to_play,limit=1,type='track')
                track_album_uri = track_info['tracks']['items'][0]['album']['uri'] # needed for context_uri to play specific song
                track_uri = track_info['tracks']['items'][0]['uri']
                self.sp.start_playback(device_id=self.device_id,context_uri=track_album_uri,offset={"uri": track_uri})
        else:
            print("Song or artist not found")

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
