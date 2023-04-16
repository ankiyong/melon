import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import os
import json
from pprint import pprint

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

# def getArtistId(artist_name):    
#     results = sp.search(q='artist:' + artist_name, type='artist')
#     if results['artists']['items']:
#         artist = results['artists']['items'][0]
#         artist_id = artist['id']
#         return artist_id
#     else:
#         print("Artist not found.")

def getArtistId(artist_name):    
    results = sp.search(q='artist:' + artist_name, type='artist')
    return results

def artistTopTrack(artist_id):
    top_track_list = []
    results = sp.artist_top_tracks(artist_id)
    results = results['tracks']
    for r in results:
        top_track = {
                        "images" : r['album']['images'][0]['url'],
                        "track_name" : r['album']['name'],
                        "realease_dete" : r['album']['release_date'],
                    }
        top_track_list.append(top_track)
    return top_track_list




def getMusic(artist):
    # artist_name =[];track_name = [];track_popularity =[];artist_id =[];track_id =[]    
    results = []    
    for i in range(0,1000,50):
        track_results = sp.search(q=f'artists:{artist}', type='track', limit=1, offset=i,market="KR")
        for i, t in enumerate(track_results['tracks']['items']):
            result = {
                "_id" : t['artists'][0]['id']+t['id'],
                "artist" : t['artists'][0]['name'],
                "track" : t['name'],
                "img" : t['album']['images'][-1]['url'],
                "artist_id" : t['artists'][0]['id'],
                "track_id" : t['id'],
                "popularity" : t['popularity']
            }
            results.append(result)
            # print(i)
    return results


def getArtist(artist):    
    results = sp.search(q=artist, type='artist',limit=1)
    # result = results['artists']['items'][0]['images'][-1]['url'] 
    # result = results['aritsts']['items'][0]['images'][1]['url']
    return results
print(getArtist("newjeans"))


# pprint(getMusic('newjeans'))
# track_results = sp.search(q='artist:newjeans', type='artist', limit=1, offset=1,market="KR")
# pprint(getArtistId("newjeans"))
# info = getArtistId("newjeans")
# followers = info['aritsts']['items'][0]['followers']['total']
# genres = info['aritsts']['items'][0]['genres'] #list반환
# img = info['aritsts']['items'][0]['images'][1]['url']
# name = info['aritsts']['items'][0]['name']
# url = info['aritsts']['items'][0]['external_urls']['spotify']