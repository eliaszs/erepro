from __future__ import print_function

import os
import grpc

import erepro.api.listings.v1.listings_pb2 as listings
import erepro.api.listings.v1.listings_pb2_grpc as listings_grpc


def test_list_listings():
    with grpc.insecure_channel(os.getenv('HOSTPORT', 'localhost:9090')) as ch:
        stub = listings_grpc.ListingsStub(ch)

        res = listings.CreateListingRequest(listing=listings.Listing(
            name='3 bed house',
            address='radison road, Isle-of-wight',
            no_beds=3,
            no_baths=1,
            price=600000,
            status='sale'
        ))
        print(res)

        print('--------')

        res = stub.ListListings(listings.ListListingsRequest(page_size=10))
        print(res)


if __name__ == '__main__':
    test_list_listings()
