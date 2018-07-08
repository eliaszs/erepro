from elasticsearch import Elasticsearch

import erepro.api.branches.v1.branches_pb2 as branches
from google.protobuf.json_format import MessageToDict, ParseDict


class BranchesRepository(object):
    def __init__(self, config):
        self.es = Elasticsearch(config.get('url'))
        self.index_name = 'branches'
        self.doc_type = 'branch'

        if not self.es.indices.exists(index=self.index_name):
            self.es.indices.create(index=self.index_name, ignore=400)
        self.es.indices.refresh(index=self.index_name)

    def ListBranches(self, page, size):
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
            yield ParseDict(hit["_source"], branches.Branch())

    def SearchBranches(self, r):
        print(r)

    def GetBranch(self, r):
        print(r)

    def CreateBranch(self, r):
        self.es.index(
            index=self.index_name,
            doc_type=self.doc_type,
            body=MessageToDict(r.branch)
        )
        return r.branch

    def UpdateBranch(self, r):
        print(r)

    def DeleteBranch(self, r):
        print(r)
