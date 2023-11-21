import subprocess
import shutil
from os import name, system
import os
import sys
# current_dir = os.getcwd()

# Probably should switch to argparse
accepted_commands = ["start", "delete"]

# print(sys.argv[0])

if (len(sys.argv) < 2):
    print("Please provide a command")
    exit(1)

if (sys.argv[1] == "start"):
    subprocess.run("python create_lab.py", shell=True)

user_base_dir = './user'
init_dir = './init_vm'
