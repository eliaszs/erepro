workspace(name = "erepro")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

http_archive(
    name = "io_bazel_rules_go",
    url = "https://github.com/bazelbuild/rules_go/releases/download/0.12.1/rules_go-0.12.1.tar.gz",
    sha256 = "8b68d0630d63d95dacc0016c3bb4b76154fe34fca93efd65d1c366de3fcb4294",
)

load("@io_bazel_rules_go//go:def.bzl", "go_rules_dependencies", "go_register_toolchains")

go_rules_dependencies()
go_register_toolchains(go_version = "host")

http_archive(
    name = "bazel_gazelle",
    url = "https://github.com/bazelbuild/bazel-gazelle/releases/download/0.12.0/bazel-gazelle-0.12.0.tar.gz",
    sha256 = "ddedc7aaeb61f2654d7d7d4fd7940052ea992ccdb031b8f9797ed143ac7e8d43",
)

load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")
gazelle_dependencies()

http_archive(
    name = "org_pubref_rules_protobuf",
    url = "https://github.com/pubref/rules_protobuf/archive/v0.8.2.tar.gz",
    strip_prefix = "rules_protobuf-0.8.2",
    sha256 = "012267bf3e2cad7a30d4e56ed4764b5457d7a829c8f037f94507222836e9a7be",
)

load("@org_pubref_rules_protobuf//go:rules.bzl", "go_proto_repositories")
go_proto_repositories()

http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "6dede2c65ce86289969b907f343a1382d33c14fbce5e30dd17bb59bb55bb6593",
    strip_prefix = "rules_docker-0.4.0",
    urls = ["https://github.com/bazelbuild/rules_docker/archive/v0.4.0.tar.gz"],
)

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_pull",
    docker_repositories = "repositories",
)

docker_repositories()

container_pull(
    name = "alpine",
    registry = "index.docker.io",
    repository = "library/alpine",
    digest = "sha256:1072e499f3f655a032e88542330cf75b02e7bdf673278f701d7ba61629ee3ebe",
)

# container_pull(
#     name = "alpine",
#     registry = "index.docker.io",
#     repository = "library/alpine",
#     digest = "sha256:1072e499f3f655a032e88542330cf75b02e7bdf673278f701d7ba61629ee3ebe",
# )
#
# container_pull(
#     name = "alpine",
#     registry = "index.docker.io",
#     repository = "library/alpine",
#     digest = "sha256:1072e499f3f655a032e88542330cf75b02e7bdf673278f701d7ba61629ee3ebe",
# )

http_archive(
    name = "grpc_ecosystem_grpc_gateway",
    url = "https://github.com/grpc-ecosystem/grpc-gateway/archive/v1.4.1.tar.gz",
    strip_prefix = "grpc-gateway-1.4.1",
    sha256 = "8f0a2db88eaef87d0a3d8a92030122ed20714004065fac2fa05fe857c097aeb3",
)

load(
    "@grpc_ecosystem_grpc_gateway//:repositories.bzl",
    grpc_gateway_repositories = "repositories",
)
grpc_gateway_repositories()

# git_repository(
#     name = "golang_sample_apis",
#     remote = "https://github.com/eliaszs/playground/bazel/golang-sample-apis",
#     # remote = "/Users/eslusarc/Workspace/src/github.com/eliaszs/playground/bazel/golang-sample/golang-sample-apis",
#     commit = "ab406f81bfd1286d9343e99b39c3620add25d6b5",
# )
#
# local_repository(
#     name = "ignore_",
#     path = "./vendor",
# )
#
#
