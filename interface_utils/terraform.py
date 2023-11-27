import subprocess
from workspace import Workspace


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

    def run_terraform_command(self, command, variables):
        terraform_command = ['terraform']
        terraform_command.extend(command)

        for key, value in variables.items():
            terraform_command.extend(['-var', key + '=' + value])

        print(terraform_command)
        subprocess.run(terraform_command)

    def get_infrastructure_variables(current_workspace: Workspace):
        terraform_variables = {
            'vpc_network_name': current_workspace.name + '-vpc',
            'subnet_name': current_workspace.name + '-subnet',
            'instance_name': current_workspace.name + '-instance',
        }
        return terraform_variables
    pass
