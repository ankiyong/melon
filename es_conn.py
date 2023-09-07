from opensearchpy import OpenSearch
# OpenSearch 호스트 및 인덱스 설정
def search(index,keyword):
  host = "https://admin:admin@localhost:9200"  
  opensearch = OpenSearch(hosts=[host],use_ssl=True,verify_certs=False)
  cnt_query = {
    "size": 10,
    "query" : {
        "match" : {
            "search.syno" : keyword
        }
      }
    }
  query = [
    {"index": index},
    {"query": {"match": {"search_syno": keyword}}},
    {"index": index},
    {"query": {"match": {"search": keyword}}},
    ]
  cnt_res = opensearch.msearch(body=cnt_query)
  return cnt_res
# print(cnt_res)

