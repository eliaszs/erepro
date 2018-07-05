from __future__ import print_function

import grpc

import erepro.api.listings.v1.listings_pb2 as listings
import erepro.api.listings.v1.listings_pb2_grpc as listings_grpc


def run():
    with grpc.insecure_channel('localhost:9090') as channel:
        stub = listings_grpc.ListingsStub(channel)
        req = listings.ListListingsRequest(page_size=10)
        res = stub.ListListings(req)
        print(res)


if __name__ == '__main__':
    run()
