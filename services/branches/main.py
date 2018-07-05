from concurrent import futures
import os
import time

import grpc

import erepro.api.branches.v1.branches_pb2 as branches
import erepro.api.branches.v1.branches_pb2_grpc as branches_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class BranchesServicer(branches_grpc.BranchesServicer):
    """Provides methods that implement functionality of branches server."""

    def __init__(self, repo=None):
        self.db = repo

    def ListBranches(self, request, context):
        print(request)

    def SearchBranches(self, request, context):
        print(request)

    def GetBranch(self, request, context):
        print(request)

    def CreateBranch(self, request, context):
        print(request)

    def UpdateBranch(self, request, context):
        print(request)

    def DeleteBranch(self, request, context):
        print(request)


def serve():
    hostport = os.getenv('HOSTPORT', '[::]:9090')

    print('Starting branches app %s' % hostport)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    branches_grpc.add_BranchesServicer_to_server(
        BranchesServicer(), server)
    server.add_insecure_port(hostport)
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
