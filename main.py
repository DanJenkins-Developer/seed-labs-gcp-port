import subprocess
import shutil
from os import name, system
import os
# current_dir = os.getcwd()


user_base_dir = './user'
init_dir = './init_vm'


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def run_terraform_command(working_dir, command, variables):
    args = ["terraform", command]

    for key, value in variables.items():
        args.extend(['-var', '{}={}'.format(key, value)])

    result = subprocess.run(args, cwd=working_dir,
                            capture_output=True, text=True)

    if result.returncode != 0:
        print(result.stderr)
    else:
        print(result.stdout)


lab_name = '/lab'

print("Enter the following details: ")
VPC_NETWORK_NAME = str(input("VPC Network Name: "))
SUBNET_NAME = str(input("Subnet Name: "))
VM_INSTANCE_NAME = str(input("VM Name: "))

user_base_dir = './user'
init_dir = './init_vm'

terraform_variables = {
    'vpc_network_name': VPC_NETWORK_NAME,
    'subnet_name': SUBNET_NAME,
    'instance_name': VM_INSTANCE_NAME
}


run_terraform_command(init_dir, 'init', {})
run_terraform_command(init_dir, 'apply', terraform_variables)
exit(1)

# user_lab_dir = user_base_dir + lab_name
# print(user_lab_dir)

# # Create user directory
# if not os.path.exists(user_base_dir):
#     os.makedirs(user_base_dir)

# # Create user lab directory
# os.makedirs(user_lab_dir)

# for item in os.listdir(init_dir):
#     item_path = os.path.join(init_dir, item)
#     if os.path.isdir(item_path):
#         shutil.copytree(item_path, os.path.join(user_lab_dir, item))
#     else:
#         shutil.copy(item_path, os.path.join(user_lab_dir, item))

# while True:

#     print("Options: ")
#     print("1. Create a new Lab")
#     print("2. Resume a Lab")
#     print("4. Delete all Labs")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         clear()
#         subprocess.call(['python', 'create_lab.py'])
#     elif choice == '2':
#         clear()
#         print("Not implemented yet")

#     elif choice == '3':
#         clear()
#         print("Not implemented yet")
#     elif choice == '4':
#         clear()
#         exit()
