.PHONY: all
all: build up e2e kill

.PHONY: build
build:
	docker-compose -f ./docker-compose.yaml build

.PHONY: services
services:
	$(MAKE) -C services build

.PHONY: up
up:
	docker-compose -f ./docker-compose.yaml up

.PHONY: e2e
e2e:
	$(MAKE) -C e2e build run

.PHONY: kill
kill:
	docker-compose -f ./docker-compose.yaml kill
