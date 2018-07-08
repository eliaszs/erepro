# -- FILE: features/steps/listings_steps.py

import grpc
from re import sub
from decimal import Decimal

import pandas as pd

from behave import given, when, then

import erepro.api.listings.v1.listings_pb2 as listings
import erepro.api.listings.v1.listings_pb2_grpc as listings_grpc


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
        df = df[['name', 'address', 'publish_date', 'status',
                 'no_beds', 'no_baths', 'price',
                 'search_views', 'norm_detail_views', 'prem_detail_views',
                 'norm_click_through_rate', 'prem_click_through_rate']]
        return df.dropna(how='all')

    context.df = clean_stuff(df)


@when('connected to a local listings grpc server at "{url}"')
def connect(context, url):
    # -- SETUP-FIXTURE PART:
    context.channel = grpc.insecure_channel(url)
    context.stub = listings_grpc.ListingsStub(context.channel)


@when('posted the list to the service')
def create(context):
    context.resps = []
    for index, row in context.df.iterrows():
        print(row['price'])
        if isinstance(row['price'], str):
            price = Decimal(sub(r'[^\d.]', '', row['price']))
        else:
            price = row['price']

        listing = listings.Listing(
            name=row['name'],
            address=row['address'],
            status=row['status'],
            no_beds=int(row['no_beds']),
            no_baths=int(row['no_baths']),
            price=int(price),
        )
        req = listings.CreateListingRequest(listing=listing)
        res = context.stub.CreateListing(req)
        assert res is not None
        context.resps.append(res)


@then('the service returns {number:d} responses with a success code')
def check_count(context, number):
    assert len(context.resps) == number


@when('queried for the list of {number:d} properties')
def list_listings(context, number):
    re = listings.ListListingsRequest(page_size=number)
    context.result = context.stub.ListListings(re)
    assert context.result is not None


@then('service will return a list of {number:d} properties to the user')
def step_impl(context, number):
    assert len(context.result.listings) == number
    # -- CLEANUP-FIXTURE PART:
    context.channel.close()
