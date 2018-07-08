.PHONY: all
all:
	$(MAKE) -C services all

.PHONY: e2e
e2e:
	$(MAKE) -C e2e all

