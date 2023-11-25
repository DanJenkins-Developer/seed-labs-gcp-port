import subprocess
import shutil
from os import name, system
import os
import sys
# current_dir = os.getcwd()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Probably should switch to argparse
accepted_commands = ["start", "delete"]

# print(sys.argv[0])

if (len(sys.argv) < 2):
    print("Please provide a command")
    exit(1)

if (sys.argv[1] == "start"):
    subprocess.run([sys.executable, "./interface_utils/create_lab_vm.py"])
elif (sys.argv[1] == "delete"):
    subprocess.run([sys.executable, "./interface_utils/destroy_lab_vm.py"])
else:
    print("command is not supported")
    exit(1)

# user_base_dir = './user'
# init_dir = './init_vm'
