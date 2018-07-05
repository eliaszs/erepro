from concurrent import futures
import os
import time

import grpc

import erepro.api.listings.v1.listings_pb2 as listings
import erepro.api.listings.v1.listings_pb2_grpc as listings_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class ListingsServicer(listings_grpc.ListingsServicer):
    """Provides methods that implement functionality of listings server."""

    def __init__(self, repo=None):
        self.db = repo

    def ListListings(self, request, context):
        print(request)

    def SearchListings(self, request, context):
        print(request)

    def GetListing(self, request, context):
        print(request)

    def CreateListing(self, request, context):
        print(request)

    def UpdateListing(self, request, context):
        print(request)

    def DeleteListing(self, request, context):
        print(request)


def serve():
    hostport = os.getenv('HOSTPORT', '[::]:9090')

    print('Starting listings app %s' % hostport)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    listings_grpc.add_ListingsServicer_to_server(
        ListingsServicer(), server)
    server.add_insecure_port(hostport)
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
