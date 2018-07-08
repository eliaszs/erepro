from concurrent import futures

import sys
import time
import grpc
import yaml

import logging

import erepro.api.branches.v1.branches_pb2_grpc as branches_grpc

from repository.branches import BranchesRepository
from services.branches import BranchesServicer

from config import parse_config


def serve(config_file):
    print('Starting app')

    config_dict = dict()
    try:
        with open(config_file, "r") as f:
            config_dict = yaml.load(f.read())
    except Exception:
        pass

    cfg = parse_config(config_dict)

    logging.basicConfig(
        level=getattr(logging, cfg.get('log')['level'].upper()),
        format=cfg.get('log')['format'])

    repo = BranchesRepository(config=cfg.get('db'))

    sc = cfg.get('server')
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=sc.get('max_workers')))
    branches_grpc.add_BranchesServicer_to_server(
        BranchesServicer(repo=repo), server)
    server.add_insecure_port(sc.get('hostport'))

    print('Listening to ' + sc.get('hostport'))
    server.start()

    try:
        while True:
            _ONE_DAY_IN_SECONDS = 60 * 60 * 24
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        print('Signal handler, shutting down the server')
        server.stop(0)


if __name__ == '__main__':
    serve(config_file=sys.argv[-1])
