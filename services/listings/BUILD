# container_image(
#     name = "listings",
#     base = "@python//image",
#     cmd = ["/api"],
#     files = ["//cmd/api"],
#     ports = ["8000"],
#     tars = ["//js:build"],
# )
#

genrule(
  name = "listings",
  visibility = ["//visibility:public"],
  srcs = glob(["**/*"]),
  cmd = "cd services/listings/ && find . && make build && touch done > $@",
  outs = ["done"],
)

