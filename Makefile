all: versions terraform

versions:
	aws --version
	aws sts get-caller-identity
	terraform --version

terraform:
	terraform -chdir=./terraform init
	terraform -chdir=./terraform apply
