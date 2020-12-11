import spotipy
import json
from datetime import date

cred = spotipy.SpotifyClientCredentials(client_id="3d6d83f030744a4b8065ffef99420660", client_secret="7576c44b974448c884702e4e316825ff")

sp = spotipy.Spotify(client_credentials_manager=cred)

countries_list = ['AD']

today = date.today().strftime("%Y-%m-%d")

file = 'raw_data/playlists/{}.txt'.format(today)

with open(file, "w") as f:
    for country in countries_list:
        play = [(pl['name'], pl['id']) for pl in sp.category_playlists("toplists", country)['playlists']['items']]
        for p in play:
            playlist = sp.playlist(p[1])
            track_list = [track['track'] for track in playlist['tracks']['items'] if track['track'] is not None]
            for track in track_list:
                track['artists'] = track['artists'][0]
                track['playlist'] = {
                    "id": playlist['id'],
                    "name": playlist['name']
                }
                json.dump(track, f, sort_keys=True)
                f.write('\n')
