import subprocess
from os import name, system


# def create_lab_vm(terraform_variables):
#     create_new_workspace()
#     run_terraform_command('init', {})
#     run_terraform_command('apply', terraform_variables)


def create_new_workspace():
    terraform_dir = '././terraform_config'
    workspace_name = str(input("Workspace Name: "))
    command = ['workspace', 'new', workspace_name]
    run_terraform_command(terraform_dir, command, {})


def run_terraform_command(working_dir, command, variables):
    # args = ["terraform", command]
    args = ["terraform"]

    if isinstance(command, list):
        args.extend(command)
    elif isinstance(command, str):
        args.append(command)

    if (command == 'apply'):
        args.append('-auto-approve')

    for key, value in variables.items():
        args.extend(['-var', '{}={}'.format(key, value)])

    # elif (command == 'workspace new'):
    #     args.append(variables)
    #     print(args)
    # result = subprocess.run(args, cwd=working_dir,
    #                         capture_output=True, text=True)
    print(args)
    result = subprocess.run(args, cwd=working_dir, text=True)

    if result.returncode != 0:
        print(result.stderr)
    else:
        print(result.stdout)

# def run_terraform_command(working_dir, command, variables):
#     args = ["terraform", command]

#     if (command == 'apply'):
#         args.append('-auto-approve')

#     for key, value in variables.items():
#         args.extend(['-var', '{}={}'.format(key, value)])

#     # result = subprocess.run(args, cwd=working_dir,
#     #                         capture_output=True, text=True)
#     result = subprocess.run(args, cwd=working_dir, text=True)

#     if result.returncode != 0:
#         print(result.stderr)
#     else:
#         print(result.stdout)


def gather_user_input():

    # lab_name = '/lab'
    print("Enter the following details: ")
    VPC_NETWORK_NAME = str(input("VPC Network Name: "))
    SUBNET_NAME = str(input("Subnet Name: "))
    VM_INSTANCE_NAME = str(input("VM Name: "))

    user_base_dir = './user'
    terraform_dir = '././terraform_config'

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
        create_new_workspace()
        run_terraform_command(terraform_dir, 'init', {})
        run_terraform_command(terraform_dir, 'apply', terraform_variables)


gather_user_input()
exit(1)
