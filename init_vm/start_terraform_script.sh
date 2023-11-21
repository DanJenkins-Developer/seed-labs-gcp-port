VPC_NETWORK_NAME="cusom-vpc-$(date +%s)"
SUBNET_NAME="custom-subnet-$(date +%s)"
INSTANCE_NAME="custom-instance-$(date +%s)"
STARTUP_SCRIPT="startup_script.sh"

terraform init
terraform apply -auto-approve \
    -var "vpc_network_name=${VPC_NETWORK_NAME}" \
    -var "subnet_name=${SUBNET_NAME}" \
    -var "instance_name=${INSTANCE_NAME}"