NAME := erepro-listings
TAG := latest

.PHONY: build
build:
	time docker build -f ./Dockerfile -t ${NAME}:${TAG} .

.PHONY: run
run:
	docker run --rm -it ${NAME}:${TAG}

.PHONY: all
test:
	pytest .
