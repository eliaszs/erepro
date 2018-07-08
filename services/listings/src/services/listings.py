import logging

import erepro.api.listings.v1.listings_pb2 as listings
import erepro.api.listings.v1.listings_pb2_grpc as listings_grpc

LOG = logging.getLogger(__name__)


class ListingsServicer(listings_grpc.ListingsServicer):
    """Provides methods that implement functionality of listings server."""

    def __init__(self, repo=None):
        self.repo = repo

    def ListListings(self, r, ctx):
        page = 0
        if r.page_token:
            page = max(int(r.page_token) + 1, 0)
        xs = self.repo.ListListings(page=page, size=r.page_size)
        return listings.ListListingsResponse(
            listings=list(xs), next_page_token=str(page+1)
        )

    def SearchListings(self, r, ctx):
        LOG.debug('r=%s', r)
        res = self.repo.SearchListings()
        LOG.debug(res)
        return listings.SearchListingsResponse()

    def GetListing(self, r, ctx):
        LOG.debug('r=%s', r)
        res = self.repo.ListListings(r)
        LOG.debug(res)
        return listings.ListListingsResponse()

    def CreateListing(self, r, ctx):
        return self.repo.CreateListing(r)

    def UpdateListing(self, r, ctx):
        LOG.debug('r=%s', r)
        res = self.repo.UpdateListing(r)
        LOG.debug(res)
        return listings.UpdateListingResponse()

    def DeleteListing(self, r, ctx):
        LOG.debug('r=%s', r)
        res = self.repo.DeleteListing(r)
        LOG.debug(res)
        return listings.DeleteListingResponse()
