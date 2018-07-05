load("@io_bazel_rules_go//go:def.bzl", "go_library")
load("@io_bazel_rules_go//proto:compiler.bzl", "go_proto_compiler")
load("@grpc_ecosystem_grpc_gateway//protoc-gen-swagger:defs.bzl", "protoc_gen_swagger")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "golang-sample-apis-proto",
    srcs = [
        "order.proto",
        "echo.proto",
    ],
    deps = [
        # "//protoc-gen-swagger/options:options_proto",
        # "@grpc_ecosystem_grpc_gateway//options:options_proto",
        # "@com_github_googleapis_googleapis//google/api:api_proto",
        "@com_github_googleapis_googleapis//google/api:api_proto",
        "@com_google_protobuf//:empty_proto",
        "@com_google_protobuf//:duration_proto",
        "@com_google_protobuf//:descriptor_proto",
        "@com_google_protobuf//:any_proto",
        "@com_google_protobuf//:timestamp_proto",
        "@com_google_protobuf//:wrappers_proto",
        "@com_google_protobuf//:struct_proto",
    ],
)

protoc_gen_swagger(
    name = "golang-sample-apis-swagger",
    proto = ":golang-sample-apis-proto",
)

go_library(
    name = "go_default_library",
    srcs = [
      "order.pb.go",
      "echo.pb.go",
      "order.pb.gw.go",
      "echo.pb.gw.go",
    ],
    importpath = "github.com/eliaszs/playground/bazel/golang-sample/golang-sample-apis/proto",
    deps = [
        "//vendor/github.com/golang/protobuf/proto:go_default_library",
        "//vendor/golang.org/x/net/context:go_default_library",
        "//vendor/google.golang.org/genproto/googleapis/api/annotations:go_default_library",
        "//vendor/google.golang.org/grpc:go_default_library",
        "@io_bazel_rules_go//proto/wkt:any_go_proto",
        "@io_bazel_rules_go//proto/wkt:descriptor_go_proto",
        "@io_bazel_rules_go//proto/wkt:duration_go_proto",
        "@io_bazel_rules_go//proto/wkt:empty_go_proto",
        "@io_bazel_rules_go//proto/wkt:struct_go_proto",
        "@io_bazel_rules_go//proto/wkt:timestamp_go_proto",
        "@io_bazel_rules_go//proto/wkt:wrappers_go_proto",
    ],
)
