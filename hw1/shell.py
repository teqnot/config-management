from filesystem import VirtualFileSystem
from commands import run_command

class ShellEmulator:
    def __init__(self, username, hostname, zip_path):
        self.username = username
        self.hostname = hostname
        self.fs = VirtualFileSystem(zip_path)

    def run_init_script(self, script_path):
        with open(script_path, 'r') as script:
            for line in script:
                self.run_command(line.strip())

    def run_command(self, command):
        return run_command(command, self.fs)
    
    def get_prompt(self):
        return f"{self.username}@{self.hostname}:{self.fs.current_directory}$ "