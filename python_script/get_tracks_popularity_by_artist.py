# coding: utf-8
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from datetime import date
import json

client_credentials_manager = SpotifyClientCredentials(client_id="3d6d83f030744a4b8065ffef99420660", client_secret="7576c44b974448c884702e4e316825ff")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Artist ID de Jul : 3IW7ScrzXmPvZhB27hmfgy
#Artist ID de Nekfeu : 4LXBc13z5EWsc5N32bLxfH
#Artist ID de Petit biscuit : 6gK1Uct5FEdaUWRWpU4Cl2

#Artiste -> liste des albums (ids) -> liste des tracks par albums-> récupérer toutes les popularité associés aux tracks

id_jul = '3IW7ScrzXmPvZhB27hmfgy'
id_nekfeu = '4LXBc13z5EWsc5N32bLxfH'
id_petitb = '6gK1Uct5FEdaUWRWpU4Cl2' 

artists_array = [id_jul, id_nekfeu, id_petitb]

def get_all_albums_id(id):
    albums_ids = []
    artist_albums = sp.artist_albums(id)
    for item in artist_albums['items']:
        albums_ids.append(item['id'])
    return albums_ids

def get_all_tracks_id(id):
    tracks_ids = []
    tracks_album = sp.album_tracks(id)
    for item in tracks_album['items']:
        tracks_ids.append(item['id'])
    return tracks_ids

def get_all_tracks_with_popularity(ids):
    tracks = []
    for item in ids:
        tracks.append((sp.track(item)))
    return tracks

track_popularity = []

for artist in artists_array:

    print("getting albums_id...")
    albums_id = get_all_albums_id(artist)
    tracks = []

    for item in albums_id:
        print("getting tracks_id...")
        tracks.append(get_all_tracks_id(item))

    for item in tracks:
        print("getting tracks...")
        track_popularity.append(get_all_tracks_with_popularity(item))

today = date.today().strftime("%Y-%m-%d")

file = 'raw_data/albums/{}.txt'.format(today)

with open(file, "w") as f:
    for item in track_popularity:
        for simple_track in item:
            simple_track_modified = simple_track
            simple_track_modified['artists'] = simple_track_modified['artists'][0]
            json.dump(simple_track_modified, f, sort_keys=True)
            f.write('\n')
