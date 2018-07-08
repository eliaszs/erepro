# container_image(
#     name = "branches",
#     base = "@python//image",
#     cmd = ["/api"],
#     files = ["//cmd/api"],
#     ports = ["8000"],
#     tars = ["//js:build"],
# )
#

genrule(
  name = "branches",
  visibility = ["//visibility:public"],
  srcs = glob(["**/*"]),
  cmd = "cd services/branches/ && find . && make build && touch done > $@",
  outs = ["done"],
)

