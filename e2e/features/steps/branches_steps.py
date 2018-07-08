# -- FILE: features/steps/branches_steps.py

import grpc

import pandas as pd

from behave import given, when, then

import erepro.api.branches.v1.branches_pb2 as branches
import erepro.api.branches.v1.branches_pb2_grpc as branches_grpc


@given('a csv file "{file}" with a list of {number:d} properties')
def parse_file(context, file, number):
    context.no_properties = number
    df = pd.read_csv(file)

    df.columns = [
        'name', 'address', 'publish_date', 'status',
        'no_beds', 'no_baths', 'price', 'branch_name',
        'branch_address', 'search_views', 'norm_detail_views',
        'prem_detail_views', 'norm_click_through_rate',
        'prem_click_through_rate']

    # TODO: write me
    def clean_stuff(df):
        # address
        # currency
        # name
        # etc
        df = df[['branch_name', 'branch_address']]
        df.columns = ['name', 'address']
        df = df.drop_duplicates(subset=['name'])
        return df.dropna(how='all')

    context.df = clean_stuff(df)


@when('connected to a local branches grpc server at "{url}"')
def connect(context, url):
    # -- SETUP-FIXTURE PART:
    context.channel = grpc.insecure_channel(url)
    context.stub = branches_grpc.BranchesStub(context.channel)


@when('posted the list to the branches service')
def create(context):
    context.resps = []
    for index, row in context.df.iterrows():
        branch = branches.Branch(
            name=row['name'],
            address=row['address'],
        )
        req = branches.CreateBranchRequest(branch=branch)
        res = context.stub.CreateBranch(req)
        assert res is not None
        context.resps.append(res)


@then('the service returns {number:d} responses with a success code')
def check_count(context, number):
    assert len(context.resps) == number


@when('queried for the {number:d} branches list')
def list_branches(context, number):
    re = branches.ListBranchesRequest(page_size=number)
    context.result = context.stub.ListBranches(re)
    assert context.result is not None


@then('service returns a list of {number:d} unique branches to the client')
def step_impl(context, number):
    assert len(context.result.branches) >= number
    # -- CLEANUP-FIXTURE PART:
    context.channel.close()
