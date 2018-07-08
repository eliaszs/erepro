from elasticsearch import Elasticsearch

import erepro.api.listings.v1.listings_pb2 as listings
from google.protobuf.json_format import MessageToDict, ParseDict


# TODO: convert protobuf spec to elasticsearch mapping
mapping = '''{
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


class ListingsRepository(object):
    def __init__(self, config):
        self.es = Elasticsearch(config.get('url'))
        self.index_name = 'listings'
        self.doc_type = 'listing'

        if not self.es.indices.exists(index=self.index_name):
            self.es.indices.create(index=self.index_name, ignore=400) # body=mapping)
            # self.es.indices.create(index=self.index_name, ignore=400, body=mapping)
        self.es.indices.refresh(index=self.index_name)

    def ListListings(self, page, size):
        res = self.es.search(
            index=self.index_name,
            doc_type=self.doc_type,
            body={
                'query': {'match_all': {}},
            },
            size=size, from_=page)

        print("Got %d Hits:" % res['hits']['total'])
        for hit in res['hits']['hits']:
            print(hit["_source"])
            yield ParseDict(hit["_source"], listings.Listing())

    def SearchListings(self, r):
        print(r)

    def GetListing(self, r):
        print(r)

    def CreateListing(self, r):
        self.es.index(
            index=self.index_name,
            doc_type=self.doc_type,
            body=MessageToDict(r.listing)
        )
        return r.listing

    def UpdateListing(self, r):
        # es.update(index='test',doc_type='test1',id='1',body={'doc':{'username':'Tom'},'doc_as_upsert':True})
        print(r)

    def DeleteListing(self, r):
        print(r)
