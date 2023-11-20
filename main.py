import subprocess
import shutil
import os

# current_dir = os.getcwd()


user_base_dir = './user'
init_dir = './init_vm'
lab_name = '/lab'

user_lab_dir = user_base_dir + lab_name
print(user_lab_dir)

# Create user directory
if not os.path.exists(user_base_dir):
    os.makedirs(user_base_dir)

os.makedirs(user_lab_dir)

for item in os.listdir(init_dir):
    item_path = os.path.join(init_dir, item)
    if os.path.isdir(item_path):
        shutil.copytree(item_path, os.path.join(user_lab_dir, item))
    else:
        shutil.copy(item_path, os.path.join(user_lab_dir, item))
