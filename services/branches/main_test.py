from __future__ import print_function

import grpc

import erepro.api.branches.v1.branches_pb2 as branches
import erepro.api.branches.v1.branches_pb2_grpc as branches_grpc


def run():
    with grpc.insecure_channel('localhost:9090') as channel:
        stub = branches_grpc.BranchesStub(channel)
        req = branches.ListBranchesRequest(page_size=10)
        res = stub.ListBranches(req)
        print(res)


if __name__ == '__main__':
    run()
