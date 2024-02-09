.DEFAULT_GOAL := default
#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y canine-classifier || :
	@pip install -e .

run_api:
	uvicorn snoop_dog.api.api:app --reload
