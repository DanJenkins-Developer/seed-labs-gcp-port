import subprocess
from os import name, system
import os


def create_lab_vm(terraform_variables):
    run_terraform_command('init', {})
    run_terraform_command('apply', terraform_variables)


def run_terraform_command(working_dir, command, variables):
    args = ["terraform", command]

    if (command == 'apply'):
        args.append('-auto-approve')

    for key, value in variables.items():
        args.extend(['-var', '{}={}'.format(key, value)])

    # result = subprocess.run(args, cwd=working_dir,
    #                         capture_output=True, text=True)
    result = subprocess.run(args, cwd=working_dir, text=True)

    if result.returncode != 0:
        print(result.stderr)
    else:
        print(result.stdout)


def gather_user_input():

    # lab_name = '/lab'
    print("Enter the following details: ")
    VPC_NETWORK_NAME = str(input("VPC Network Name: "))
    SUBNET_NAME = str(input("Subnet Name: "))
    VM_INSTANCE_NAME = str(input("VM Name: "))

    user_base_dir = './user'
    # init_dir = './init_vm'
    init_dir = os.getcwd()
    print(init_dir)
    terraform_variables = {
        'vpc_network_name': VPC_NETWORK_NAME,
        'subnet_name': SUBNET_NAME,
        'instance_name': VM_INSTANCE_NAME
    }

    print("Confirmed details: ")
    print("VPC Network Name: " + VPC_NETWORK_NAME)
    print("Subnet Name: " + SUBNET_NAME)
    print("VM Name: " + VM_INSTANCE_NAME)
    confirmation = str(input("Is this correct? (y/n): "))

    if (confirmation == "y" or confirmation == "Y" or confirmation == "yes" or confirmation == "Yes" or confirmation == "YES"):
        run_terraform_command(init_dir, 'init', {})
        run_terraform_command(init_dir, 'apply', terraform_variables)


gather_user_input()
exit(1)
