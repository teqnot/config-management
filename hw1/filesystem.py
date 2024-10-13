import zipfile
import os
import sys
import time
from datetime import datetime
#from io import StringIO

class VirtualFileSystem:
    def __init__(self, zip_path):
        self.zip_path = zip_path
        self.file_system = {}
        self.current_directory = "/"
        self.log_file_path = "vfs/var/log/system.log"
        self.load_file_system()

    def load_file_system(self):
        with zipfile.ZipFile(self.zip_path, 'r') as arch:
            for file in arch.namelist():
                self._add_to_tree(file)

    def _add_to_tree(self, path):
        dirs = path.split('/')
        current = self.file_system

        for part in dirs:
            if part not in current:
                current[part] = {}
            current = current[part]

    def get_current_directory(self):
        dirs = self.current_directory.strip("/").split("/")
        current = self.file_system

        for part in dirs:
            if part:
                current = current.get(part, {})
        
        return current
    
    def change_directory(self, path):
        if path == "/":
            self.current_directory = "/"
        elif path == "..":
            if self.current_directory != "/":
                self.current_directory = os.path.dirname(self.current_directory)
        else:
            new_dir = os.path.join(self.current_directory, path).replace("\\", "/")
            if new_dir in self.get_all_paths():
                self.current_directory = new_dir
                self.write_log(f"cd {path}")
            else:
                self.write_log(f"[ Directory {path} was not found. ]")
                raise FileNotFoundError(f"[ Directory {path} was not found. ]")
            
    def get_all_paths(self):
        paths = []
        def traverse(fs, path=""):
            for item in fs:
                new_path = f"{path}/{item}".replace("\\", "/")
                paths.append(new_path)
                if isinstance(fs[item], dict):
                    traverse(fs[item], new_path)
        traverse(self.file_system)
        return paths
    
    def ls(self):
        current_dir = self.get_current_directory()
        self.write_log("ls")
        result = [(str(k) + "\n" if (i > 0 and i < len(current_dir.keys()) - 1) else str(k)) for i, k in enumerate(current_dir)]
        return "".join(result)
    
    def wc(self, file_path):
        full_path = os.path.join(self.current_directory, file_path).replace("\\", "/")
        if full_path in self.get_all_paths():
            with zipfile.ZipFile(self.zip_path, 'r') as arch:
                with arch.open(full_path.lstrip("/")) as file:
                    content = file.read().decode("utf-8")
                    lines = content.count("\n") + 1
                    words = len(content.split())
                    chars = len(content)
                    result = f"[ lines - {lines} | words - {words} | chars - {chars} | file name - {file_path} ]"
            self.write_log(f"wc {file_path} -> {result}")
            return result
        else:
            self.write_log(f"[ File {file_path} was not found. ]")
            raise FileNotFoundError(f"[ File {file_path} was not found. ]")
        
    def du(self, path="."):
        try:
            current_dir = self.get_current_directory()
            size = 0
            if path == ".":
                size = self._get_directory_size(current_dir)
            else:
                full_path = os.path.join(self.current_directory, path).replace("\\", "/")
                if full_path in self.get_all_paths():
                    size = self._get_directory_size(self.get_current_directory())
                else:
                    raise FileNotFoundError(f"[ Path {path} was not found. ]")
            result = f"{size} bytes"
            self.write_log(f"du {path} -> {result}")
            return result
        except FileNotFoundError as e:
            self.write_log(str(e))
            raise
    
    def _get_directory_size(self, directory):
        size = 0
        with zipfile.ZipFile(self.zip_path, 'r') as arch:
            for file_info in arch.infolist():
                if file_info.filename.startswith(self.current_directory.strip('/')):
                    size += file_info.file_size
        return size
    
    def exit_shell(self):
        self.write_log("exit")
        time.sleep(1.0)
        sys.exit()

    def write_log(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {message}\n"

        log_content = ""
        try:
            with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
                with zip_ref.open(self.log_file_path) as log_file:
                    log_content = log_file.read().decode('utf-8')
        except KeyError:
            pass

        log_content += log_entry

        temp_zip_path = self.zip_path + ".tmp"

        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            with zipfile.ZipFile(temp_zip_path, 'w') as new_zip:
                for item in zip_ref.infolist():
                    if item.filename != self.log_file_path:
                        new_zip.writestr(item, zip_ref.read(item.filename))
                new_zip.writestr(self.log_file_path, log_content)

        os.replace(temp_zip_path, self.zip_path)