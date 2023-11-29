import subprocess
import os
from .workspace import Workspace


class Terraform:

    def __init__(self):

        # Set the terraform directory
        self.terraform_dir = '././terraform_config'

        # Create the default workspace
        default_workspace = Workspace('default')
        self.workspaces = [default_workspace]
        self.current_workspace: Workspace = default_workspace

    def create_workspace(self, name):

        # Check if the workspace already exists
        if (name in self.workspaces):
            print("Workspace already exists")
            return

        # Create the workspace
        command = ['workspace', 'new', name]
        self.run_terraform_command(command, {})

        # Add the workspace to the list of workspaces
        workspace = Workspace(name)
        self.workspaces.append(workspace)

    def delete_workspace(self, name):
        command = ['workspace', 'delete', name]
        self.run_terraform_command(command, {})
        workspace = Workspace(name)
        self.workspaces.remove(workspace)

    def select_workspace(self, name):
        command = ['workspace', 'select', name]
        self.run_terraform_command(command, {})
        workspace = Workspace(name)
        self.current_workspace = workspace

    def get_current_workspace(self):
        return self.current_workspace

    def initialize_workspace(self):
        command = ['init']
        self.run_terraform_command(command, {})

    def apply_workspace(self):
        command = ['apply']
        self.run_terraform_command(
            command, self.get_infrastructure_variables(self.current_workspace))
        # self.lab_running = True

    def create_infrastructure(self, workspace_name):
        print(workspace_name)
        self.select_workspace(workspace_name)
        self.apply_workspace()
        self.initialize_workspace()

    def destroy_infrastructure(self):
        command = ['destroy']
        self.run_terraform_command(
            command, {})
        # self.lab_running = False

    def run_terraform_command(self, command, variables):
        working_dir = self.terraform_dir
        # args = ["terraform", command]
        args = ["terraform"]

        if isinstance(command, list):
            args.extend(command)
        elif isinstance(command, str):
            args.append(command)

        if (command == 'apply' or command == 'destroy'):
            args.append('-auto-approve')

        for key, value in variables.items():
            args.extend(['-var', '{}={}'.format(key, value)])

        # print(args)
        result = subprocess.run(args, cwd=working_dir, text=True)

        if result.returncode != 0:
            print(result.stderr)
        else:
            print(result.stdout)

    def get_infrastructure_variables(current_workspace: Workspace):
        terraform_variables = {
            'vpc_network_name': current_workspace.name + '-vpc',
            'subnet_name': current_workspace.name + '-subnet',
            'instance_name': current_workspace.name + '-instance',
        }
        return terraform_variables
    pass
