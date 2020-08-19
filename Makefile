.PHONY: test clean help

# Configuration variables
PROJECT := pyrunner-api
TESTDIR := tests
REQUIREMENTS := requirements.txt
VENV_NAME := virtualenv
VENV_ACTIVATE := $(VENV_NAME)/bin/activate


######### User targets #########

virtualenv: ## Create a virtual environment and install required packages into it
	# Instal virtualenv package if not installed
	@python3 -m pip show virtualenv > /dev/null || python3 -m pip install virtualenv

	@[ -d $(VENV_NAME) ] || python3 -m virtualenv $(VENV_NAME)

	@. ./$(VENV_ACTIVATE) && \
    	python3 -m pip install --upgrade pip > /dev/null && \
    	python3 -m pip install -r $(REQUIREMENTS) > /dev/null

test: virtualenv## Run the unit tests
	@. ./$(VENV_ACTIVATE) && \
		python3 -m pytest --rootdir=${TESTDIR}

clean:
	@rm -r virtualenv

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
