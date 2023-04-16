import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from fastapi import FastAPI, Query,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import uvicorn
# from get_music import *
from es import *
import requests
import os
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM
from elasticsearch import Elasticsearch,helpers
# from es import *

# res = getMusic("newjeans")
# print(res)
# print(searchData("newjeans")['hits']['total']['value'])
# insertData(res)
# res = insertData(res)
# for i in res:
    # print(i)

# track_results = sp.search(q='artists:newjeans', type='artist', limit=1, offset=1,market="KR")
# print(track_results)



def search_a(query,artist):
    with open(f'./es/{query}.json') as f:
            doc = f.read()
    es = Elasticsearch('https://192.168.52.196:9220', http_auth=('elastic','cnT_mp*rlmOAMiL244u0'), verify_certs=False)
    artist = artist
    formatted_json_string = doc % artist
    doc = json.loads(formatted_json_string)
    res = es.search(index="tracks_test",body=doc)
    print(res)

class Agent:
    def __init__(self, host: str, http_auth: str):
        self.host: str = host
        self.http_auth: str = http_auth
    
    def __get_es(self) -> Elasticsearch:
        return Elasticsearch(self.host, http_auth=('elastic', self.http_auth), verify_certs=False)

    def search_data(self,q):
        res = self.__get_es().search(index="tracks_test",body={'size':1000,'query':{'match':{'artist':q}}})
        return res
        # print(res)

    def insert_data(self, tracks):
        resultDict = []
        for data in tracks:
            id = data["_id"]
            del data["_id"]
            result = {"_index": "tracks_test", "_id" : id,"_source": data}
            resultDict.append(result)
        helpers.bulk(self.__get_es(), resultDict)

def getArtist(artist):    
    results = sp.search(q=artist, type='artist',limit=1)
    # result = results['artists']['items'][0]['images'][-1]['url'] 
    # result = results['aritsts']['items'][0]['images'][1]['url']
    return results

if __name__ == "__main__":
    # q = "NewJeans"
    # agent: Agent = Agent('https://192.168.52.196:9220', 'cnT_mp*rlmOAMiL244u0')
    # data = agent.search_data(q)
    # # for i in data:
    #     # print(i)
    # datas = data['hits']['hits']
    # for i in datas:
    #     print(i)
    # # agent.insert_data(tracks)

