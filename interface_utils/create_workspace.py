import subprocess
from os import name, system


def create_new_workspace():
    terraform_dir = '././terraform_config'
    workspace_name = str(input("Workspace Name: "))
    run_terraform_command(terraform_dir, 'workspace new', workspace_name)
    pass


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
