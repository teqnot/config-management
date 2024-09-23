import sys

def run_command(command, fs):
    command = command.strip()
    if not command:
        return ""
    
    parts = command.split()
    cmd = parts[0]

    try:
        if cmd == "ls":
            return fs.ls()
        elif cmd == "cd":
            if len(parts) > 1:
                fs.change_directory(parts[1])
            else:
                return "[ Usage: cd /path/to/directory ]"
        elif cmd == "wc":
            return fs.wc(parts[1])
        elif cmd == "du":
            return fs.du(parts[1] if len(parts) > 1 else ".")
        elif cmd == "exit":
            return fs.exit_shell()
        
        else:
            return f"[ Command {cmd} was not found. ]"
    except Exception as e:
        return str(e)