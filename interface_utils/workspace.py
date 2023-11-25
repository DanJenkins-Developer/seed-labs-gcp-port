import subprocess


class Workspace:
    terraform_dir = '././terraform_config'

    def __init__(self, name):
        self.name = name
        self.lab_vm = None
        self.lab_running = False
        # self.create_workspace()

    def create_workspace(self):

        print(self.name)
        command = ['workspace', 'new', self.name]
        self.run_terraform_command(command, {})

    def delete_workspace(self):
        command = ['workspace', 'delete', self.name]
        self.run_terraform_command(command, {})

    def select_workspace(self):
        command = ['workspace', 'select', self.name]
        self.run_terraform_command(command, {})

    def list_workspaces(self):
        command = ['workspace', 'list']
        self.run_terraform_command(command, {})

    def initialise_workspace(self):
        command = ['init']
        self.run_terraform_command(command, {})

    def apply_workspace(self):
        command = ['apply']
        self.run_terraform_command(
            command, self.get_infrastructure_variables())
        self.lab_running = True

    def destroy_workspace(self):
        command = ['destroy']
        self.run_terraform_command(
            command, {})
        self.lab_running = False

    def get_infrastructure_variables(self):
        terraform_variables = {
            'vpc_network_name': self.name + '-vpc',
            'subnet_name': self.name + '-subnet',
            'instance_name': self.name + '-instance',
        }

        return terraform_variables

    def create_lab_vm(self):
        self.create_workspace()
        self.initialise_workspace()
        self.apply_workspace()
        self.lab_running = True

    def destroy_lab_vm(self):
        self.destroy_workspace()
        # self.delete_workspace()
        self.lab_running = False

    def run_terraform_command(self, command, variables):

        working_dir = self.terraform_dir
        # args = ["terraform", command]
        args = ["terraform"]

        if isinstance(command, list):
            args.extend(command)
        elif isinstance(command, str):
            args.append(command)

        print(args)

        # if (command == 'apply'):
        args.append('-auto-approve')

        for key, value in variables.items():
            args.extend(['-var', '{}={}'.format(key, value)])

        # print(args)
        result = subprocess.run(args, cwd=working_dir, text=True)

        if result.returncode != 0:
            print(result.stderr)
        else:
            print(result.stdout)
    pass
