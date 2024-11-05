import subprocess

def listAllGitObjects():
    result = subprocess.run(
        ["git", "rev-list", "--all", "--objects"],
        capture_output=True,
        text=True,
        check=True)
    
    for line in result.stdout.splitlines():
        parts = line.split()
        obj_hash = parts[0]
        obj_path = parts[1] if len(parts) > 1 else None

        print(f"Object hash: {obj_hash}")
        if obj_path:
            print(f"Path: {obj_path}")

        obj_content = subprocess.run(
            ["git", "cat-file", "-p", obj_hash],
            capture_output=True,
            text=True,
            check=True)
        
        print("Content:")
        print(obj_content.stdout)
        print("-" * 40)

listAllGitObjects()