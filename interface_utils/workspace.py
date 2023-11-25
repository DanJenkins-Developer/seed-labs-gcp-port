import subprocess


class Workspace:
    terraform_dir = '././terraform_config'

    def __init__(self, name):
        self.name = name
        self.lab_vm = None
        self.lab_running = False
        self.create_workspace()

    def create_workspace(self):

        command = ['workspace', 'new', self.name]
        self.run_terraform_command(self, command, {})

    def delete_workspace(self):
        command = ['workspace', 'delete', self.name]
        self.run_terraform_command(self, command, {})

    def select_workspace(self):
        command = ['workspace', 'select', self.name]
        self.run_terraform_command(self, command, {})

    def initialise_workspace(self):
        command = ['init']
        self.run_terraform_command(self, command, {})

    def apply_workspace(self, variables):
        command = ['apply']
        self.run_terraform_command(self, command, variables)
        self.lab_running = True

    def run_terraform_command(self, command, variables):

        working_dir = self.terraform_dir
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

        # print(args)
        result = subprocess.run(args, cwd=working_dir, text=True)

        if result.returncode != 0:
            print(result.stderr)
        else:
            print(result.stdout)
    pass
