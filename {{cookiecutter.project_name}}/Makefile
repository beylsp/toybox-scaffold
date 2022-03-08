SHELL := /bin/bash # Use bash syntax

define HELP_TEXT
{{cookiecutter.project_title}}
===

Usage:

> make setup          # Prepare dependencies
{%- if cookiecutter.use_db == "yes" %}
> make init           # Create database
{%- endif %}
> make develop        # Run the dev server
> make clean          # Clean the project

endef

export PIPENV_VENV_IN_PROJECT=1

ENVPATH=${VIRTUAL_ENV}
PIPENV=pipenv
{%- if cookiecutter.use_db == "yes" %}
SYSTEM_DEPENDENCIES=curl make python3-dev libpq-dev sqlite3 python3-pip
{%- else %}
SYSTEM_DEPENDENCIES=curl make python3-dev python3-pip
{%- endif %}

ifeq ($(ENVPATH),)
  ENVPATH=.venv
endif

##
# Print help test
##
help:
	$(info ${HELP_TEXT})

##
# Prepare the project
##
setup:
	# Install missing dependencies
	if ! dpkg -s ${SYSTEM_DEPENDENCIES} &> /dev/null; then \
		sudo apt update && sudo apt install -y ${SYSTEM_DEPENDENCIES}; \
	fi

	# Install Node.js globally
	type node &> /dev/null || sudo snap install node --classic --channel=16

	# Install requirements
	yarn install

	# Install pipenv globally (also installs virtualenv)
	type pipenv &> /dev/null || sudo python3 -m pip install pipenv

	# Create virtual env folder, if not already in one
	if [ -z ${VIRTUAL_ENV} ]; then ${PIPENV} --three; fi

	# Install requirements into virtual env
	${PIPENV} install

{%- if cookiecutter.use_db == "yes" %}
##
# Create database
##
init:
	${PIPENV} run flask db init
	${PIPENV} run flask db upgrade
{%- endif %}

##
# Start the development server
##
develop:
	yarn build
	${PIPENV} run flask run

##
# Clean the project
##
clean:
	yarn clean
	rm -f *.db
	rm -rf ${ENVPATH}

# Non-file make targets
{%- if cookiecutter.use_db == "yes" %}
.PHONY: help setup init develop clean
{%- else %}
.PHONY: help setup develop clean
{%- endif %}