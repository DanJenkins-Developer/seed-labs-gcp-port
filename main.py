import subprocess
import shutil
from os import name, system
import os
import sys
# from interface_utils.workspace import Workspace
from interface_utils.terraform import Terraform

# current_dir = os.getcwd()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

terraform = Terraform()


# terraform.create_workspace('test2')
# print(terraform.get_current_workspace().name)

# terraform.select_workspace('default')
print(terraform.get_current_workspace().name)
terraform.create_workspace('test2')
terraform.create_infrastructure('test2')

# Probably should switch to argparse
# accepted_commands = ["start", "delete"]

# # print(sys.argv[0])

# if (len(sys.argv) < 2):
#     print("Please provide a command")
#     exit(1)


# if (sys.argv[1] == "start"):
#     if (len(sys.argv) < 3):
#         print("Please provide a workspace name")
#         exit(1)

#     workspace_name = sys.argv[2]
#     workspace = Workspace(workspace_name)
#     print(workspace.name)
#     # workspace.create_lab_vm()
#     workspace.create_workspace()

#     # print(workspace_name)
#     # subprocess.run([sys.executable, "./interface_utils/create_lab_vm.py"])
# elif (sys.argv[1] == "delete"):
#     if (len(sys.argv) < 3):
#         print("Please provide a workspace name")
#         exit(1)

#     workspace_name = sys.argv[2]
#     workspace = Workspace(workspace_name)
#     workspace.delete_workspace()
#     # subprocess.run([sys.executable, "./interface_utils/destroy_lab_vm.py"])
# else:
#     print("command is not supported")
#     exit(1)

# user_base_dir = './user'
# init_dir = './init_vm'
