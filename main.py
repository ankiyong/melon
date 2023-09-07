# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# import pandas as pd
from fastapi import FastAPI, Query,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import uvicorn
# from get_music import *
# from es import *
from es_conn import *
import requests
import os
# from elasticapm.contrib.starlette import make_apm_client, ElasticAPM
# from elasticsearch import Elasticsearch,helpers
from fastapi.staticfiles import StaticFiles

# SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
# SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')

# agent: Agent = Agent('https://192.168.52.196:9220', 'cnT_mp*rlmOAMiL244u0')

templates = Jinja2Templates(directory='./templates/')

app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")

# apm_config = {
#     "SERVICE_NAME": "melon",
#     "SERVER_URL": "http://localhost:8200",
#     "ENVIRONMENT": "dev",
#     "GLOBAL_LABELS": "platform=Platform, application=Application",
# }

# apm = make_apm_client(apm_config)
# app.add_middleware(ElasticAPM,client=apm)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

    
@app.get("/exist")
async def exist(q:str):
    track_list = []
    search_res = search("dict_test",q)
    data = search_res['hits']['hits'][0]["_source"]
    return data
    # es_res = agent.search_data("artist",q)
    # if es_res['hits']['total']['value'] == 0:
        # res = getArtist(q);agent.insert_data(res)
        # return res    
    # else:
        # data = es_res['hits']['hits'][0]["_source"]
        # return data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)