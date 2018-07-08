from __future__ import print_function

import os
import grpc

import erepro.api.branches.v1.branches_pb2 as branches
import erepro.api.branches.v1.branches_pb2_grpc as branches_grpc


def run():
    with grpc.insecure_channel(os.getenv('HOSTPORT', 'localhost:9090')) as ch:
        stub = branches_grpc.BranchesStub(ch)
        res = stub.ListBranches(branches.ListBranchesRequest(page_size=10))
        assert res is not None
        print(res)


if __name__ == '__main__':
    run()
