from datetime import datetime
from elasticsearch import Elasticsearch

mapping = '''
{
  "mappings":{
    "logs_june":{
      "_timestamp":{
        "enabled":"true"
      },
      "properties":{
        "logdate":{
          "type":"date",
          "format":"dd/MM/yyy HH:mm:ss"
        }
      }
    }
  }
}'''


def test():
    es = Elasticsearch()

    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }
    res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
    print(res['result'])

    res = es.get(index="test-index", doc_type='tweet', id=1)
    print(res['_source'])

    es.indices.refresh(index="test-index")

    res = es.search(index="test-index", body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
