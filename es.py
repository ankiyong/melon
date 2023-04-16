import json
import os
from elasticsearch import Elasticsearch,helpers

def searchData(q):
    es = Elasticsearch('https://192.168.52.196:9220', http_auth=('elastic','cnT_mp*rlmOAMiL244u0'), verify_certs=False)
    res = es.search(index="tracks_test",body={'query':{'match':{'artist.keyword':q}}})
    # cnt = res['hits']['total']['value']
    return res
    # else:
        # return "nothing"



def insertData(tracks):
    es = Elasticsearch('https://192.168.52.196:9220', http_auth=('elastic','cnT_mp*rlmOAMiL244u0'), verify_certs=False)
    resultDict = []
    for data in tracks:
        id = data["_id"]
        del data["_id"]
        result = {"_index": "tracks_test", "_id" : id,"_source": data}
        resultDict.append(result)
    helpers.bulk(es, resultDict)


class Agent:
    def __init__(self, host: str, http_auth: str):
        self.host: str = host
        self.http_auth: str = http_auth
    
    def __get_es(self) -> Elasticsearch:
        return Elasticsearch(self.host, http_auth=('elastic', self.http_auth), verify_certs=False)

    def search_data(self,index,q):
        with open(f'./es/{index}.json') as f:
            doc = f.read()
        artist = q
        formatted_json_string = doc % artist
        doc = json.loads(formatted_json_string)
        res = self.__get_es().search(index=index,body=doc)
        return res

    def bulk_insert(self, tracks):
        resultDict = []
        for data in tracks:
            id = data["_id"]
            del data["_id"]
            result = {"_index": "artist", "_id" : id,"_source": data}
            resultDict.append(result)
        helpers.bulk(self.__get_es(), resultDict)
    
    def insert_data(self,info):        
        es = self.__get_es()
        es.index(index="artist",body=info)


# if __name__ == "__main__":
# #     tracks = "1"
#     agent: Agent = Agent('https://192.168.52.196:9220', 'cnT_mp*rlmOAMiL244u0')
#     res = agent.search_data("artist","아이유")
#     if res['hits']['total']['value'] == 0:        
#         print("res")

#     # agent.insert_data(tracks)

