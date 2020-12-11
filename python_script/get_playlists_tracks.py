import spotipy
import json
from datetime import date

cred = spotipy.SpotifyClientCredentials(client_id='client_id', client_secret='client_secret')

sp = spotipy.Spotify(client_credentials_manager=cred)

countries_list = ['AD', 'AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'EC',
                  'SV', 'EE', 'FI', 'FR', 'DE', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'ID', 'IE', 'IT', 'JP', 'LV', 'LI',
                  'LT', 'LU', 'MY', 'MT', 'MX', 'MC', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG',
                  'ES', 'SK', 'SE', 'CH', 'TW', 'TR', 'GB', 'US', 'UY']

today = date.today().strftime("%Y-%m-%d")

file = '{}.txt'.format(today)
s = set()
with open(file, "w") as f:
    for country in countries_list:
        play = [(pl['name'], pl['id']) for pl in sp.category_playlists("toplists", country)['playlists']['items']]
        for p in play:
            if p[1] not in s:
                s.add(p[1])
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
