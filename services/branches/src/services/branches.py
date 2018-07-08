import logging

import erepro.api.branches.v1.branches_pb2 as branches
import erepro.api.branches.v1.branches_pb2_grpc as branches_grpc

LOG = logging.getLogger(__name__)


class BranchesServicer(branches_grpc.BranchesServicer):
    """Provides methods that implement functionality of branches server."""

    def __init__(self, repo=None):
        self.repo = repo

    def ListBranches(self, r, ctx):
        page = 0
        if r.page_token:
            page = max(int(r.page_token) + 1, 0)
        xs = self.repo.ListBranches(page=page, size=r.page_size)
        return branches.ListBranchesResponse(
            branches=list(xs), next_page_token=str(page+1)
        )

    def SearchBranches(self, r, ctx):
        LOG.debug('r=%s', r)
        res = self.repo.SearchBranches()
        LOG.debug(res)
        return branches.SearchBranchesResponse()

    def GetBranch(self, r, ctx):
        LOG.debug('r=%s', r)
        res = self.repo.ListBranches(r)
        LOG.debug(res)
        return branches.ListBranchesResponse()

    def CreateBranch(self, r, ctx):
        return self.repo.CreateBranch(r)

    def UpdateBranch(self, r, ctx):
        LOG.debug('r=%s', r)
        res = self.repo.UpdateBranch(r)
        LOG.debug(res)
        return branches.UpdateBranchResponse()

    def DeleteBranch(self, r, ctx):
        LOG.debug('r=%s', r)
        res = self.repo.DeleteBranch(r)
        LOG.debug(res)
        return branches.DeleteBranchResponse()
