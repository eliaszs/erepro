filegroup(
    name = "build",
    srcs = [
        "//services/listings",
    ],
)

load("@io_bazel_rules_go//go:def.bzl", "gazelle", "go_prefix")

go_prefix("github.com/eliaszs/erepro")

gazelle(
    name = "gazelle",
    command = "fix",
    external = "vendored",
    prefix = "github.com/eliaszs/erepro",
)

# load("@io_bazel_rules_docker//container:container.bzl", "container_image", "container_push")

# container_image(
#     name = "lasersteak",
#     base = "@alpine//image",
#     cmd = ["/api"],
#     files = ["//cmd/api"],
#     ports = ["8000"],
#     tars = ["//js:build"],
# )
#
# container_push(
#     name = "lasersteak-publish",
#     format = "Docker",
#     image = ":lasersteak",
#     registry = "localhost:5000",
#     repository = "lasersteak",
#     stamp = True,
#     tag = "{BUILD_USER}",
# )
#
