.PHONY: dep
dep:
	dep ensure -v -update

NAME := erepro-listings-gw

.PHONY: build
build:
	time docker build -f ./Dockerfile -t ${NAME}:latest .

