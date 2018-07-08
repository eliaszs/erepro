.PHONY: prep
prep:
	rm -rf erepro-apis googleapis
	git clone --recursive https://github.com/googleapis/googleapis.git
	git clone --recursive https://github.com/eliaszs/erepro-apis.git

.PHONY: all
all:
	$(MAKE)	-C branches build
	$(MAKE) -C branches-gw build
	$(MAKE) -C listings build
	$(MAKE) -C listings-gw build
