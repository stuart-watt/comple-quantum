###########################
## Environment variables ##
###########################
include .env

export ALIAS = quantum 		# must match name field in environment.yaml

export PROJECT_ID = $(GCP_PROJECT_ID)
export GOOGLE_APPLICATION_CREDENTIALS ?= $(HOME)/$(CREDENTIALS)

#############
## Install ##
#############

mamba:
	mamba env update -n $(ALIAS) --file environment.yml --prune \
		|| \
	mamba env create --file environment.yml
