.PHONY: help dev clean coverage check serve test test-staging test-dev superuser migrate create-db refresh-db todos token bench pytest \
		aws_ecr_update_auth_credentials aws_ecr_production_image_update aws_ecr_uat_image_update aws_eb_uat_deploy aws_eb_production_deploy \
		docker_build_local docker_build_uat docker_build_production docker_run_local

DJANGO_COMMAND = python manage.py

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@egrep '^(.+)\:.*?#+\ *(.+)' ${MAKEFILE_LIST} | column -t -c 2 -s '#'

run: ## To run project locally
	@echo "--> \033[0;32mUping in the port 8000\033[0m"
	docker-compose up

down: ## To run project locally
	@echo "--> \033[0;32mUping in the port 8000\033[0m"
	docker-compose down

build: ## To build with docker-compose
	export DOCKER_BUILDKIT=1;docker-compose build

build-no-cache:  ## To build with docker-compose and without cache
	export DOCKER_BUILDKIT=1;docker-compose build --no-cache

install-requirements:  ## To install requirements
	pip install -r requirements.txt

migrations:  ## To create migrations
	@echo "--> \033[0;32mCreating migrations\033[0m"
	docker-compose run server $(DJANGO_COMMAND) makemigrations

migrate:  ## To migrate
	@echo "--> \033[0;32mMigrating\033[0m"
	docker-compose run server $(DJANGO_COMMAND) migrate

superuser: ## To create super user
	@echo "--> \033[0;32mIntroduce your local credentials:\033[0m"
	docker-compose run server $(DJANGO_COMMAND) createsuperuser
