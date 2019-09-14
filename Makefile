CUSTOMERS_FILE_NAME := customers.txt
CUSTOMERS_FILE      := https://s3.amazonaws.com/intercom-take-home-test/$(CUSTOMERS_FILE_NAME)
INPUT_FILE_NAME     ?= $(CUSTOMERS_FILE_NAME)
OUTPUT_FILE_NAME    ?= output.txt
REFERENCE_LAT       ?= 53.339428
REFERENCE_LONG      ?= -6.257664
RADIUS              ?= 100

$(CUSTOMERS_FILE_NAME):
	wget $(CUSTOMERS_FILE) -O $(CUSTOMERS_FILE_NAME)

.PHONY: build
build: $(CUSTOMERS_FILE_NAME)
	pip install -r requirements.txt
	pip install -e .

.PHONY: run
run:
	python geo_curator/run.py \
        --customers-file $(CUSTOMERS_FILE_NAME) \
        --output-file $(OUTPUT_FILE_NAME) \
        --reference-lat $(REFERENCE_LAT) \
        --reference-long $(REFERENCE_LONG) \
        --radius $(RADIUS)

.PHONY: test
test:
	python -Wignore -m unittest discover
