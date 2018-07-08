# -- FILE: features/environment.py

import grpc

from behave import fixture, use_fixture

import erepro.api.listings.v1.listings_pb2_grpc as listings_grpc


@fixture
def listings_stub(context, hostport='localhost:9090'):
    # -- SETUP-FIXTURE PART:
    context.channel = grpc.insecure_channel(hostport)
    context.stub = listings_grpc.ListingsStub(context.channel)
    yield context.stub

    # -- CLEANUP-FIXTURE PART:
    context.stub.close()
    context.channel.close()


def before_all(context):
    use_fixture(listings_stub, context)
    # -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.


# def before_feature(context, feature):
#     model.init(environment='test')
