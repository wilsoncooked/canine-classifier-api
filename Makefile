.DEFAULT_GOAL := default
#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y canine-classifier || :
	@pip install -e --no-cache-dir .

run_api:
	uvicorn snoop_dog.api.api:app --reload

docker_build:
	docker build -t ${GAR_IMAGE} .

docker_run:
	docker run -it -e PORT=8000 -p 8000:8000 ${GAR_IMAGE}

docker_build_prod:
	docker build -t ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/canine-classifier/${GAR_IMAGE}:prod .

docker_run_prod:
	docker run -it -e PORT=8000 -p 8000:8000 --env-file .env ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/canine-classifier/${GAR_IMAGE}:prod

docker_push_prod:
	docker push ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/canine-classifier/${GAR_IMAGE}:prod

docker_deploy_prod:
	gcloud run deploy --image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/canine-classifier/${GAR_IMAGE}:prod --region ${GCP_REGION} --memory ${GAR_MEMORY}  --env-vars-file .env.yaml

artifacts_create_repo:
	gcloud artifacts repositories create canine-classifier --repository-format=docker --location=${GCP_REGION} --description="Repository for storing canine-classifier images"
