from shell import ShellEmulator
from gui import ShellGUI
import argparse

def main():
    parser = argparse.ArgumentParser(description="Shell Emulator")
    parser.add_argument('--username', required=True)
    parser.add_argument('--hostname', required=True)
    parser.add_argument('--zip_path', required=True)
    parser.add_argument('--init_script', required=True)
    args = parser.parse_args()

    shell = ShellEmulator(args.username, args.hostname, args.zip_path)

    gui = ShellGUI(shell)
    gui.run_init_script(args.init_script)
    gui.run()

if __name__ == "__main__":
    main()