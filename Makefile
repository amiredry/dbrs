SHELL = /bin/bash
VE ?= ./ve
PIP ?= $(VE)/bin/pip
REQUIREMENTS ?= requirements.txt


create:
	@echo "Installing python virtual env at $(VE)"
	rm -rf $(VE)
	python3 -m venv $(VE)
	$(PIP) install --requirement $(REQUIREMENTS)

getdata:
	@echo "Downloading data..."
	$(VE)/bin/python3 ./dbrs.py
