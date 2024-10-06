import unittest
import zipfile
import os
from io import BytesIO
from shell import ShellEmulator
from filesystem import VirtualFileSystem

class TestVirtualFileSystem(unittest.TestCase):

    def setUp(self):
        self.test_zip_data = "vfs.zip"
        self.shell = ShellEmulator("user", "host", self.test_zip_data)
        self.vfs = VirtualFileSystem(self.test_zip_data)

    def test_cd_root(self):
        self.vfs.change_directory("/")
        self.assertEqual(self.vfs.current_directory, "/")

    def test_cd_home(self):
        self.vfs.change_directory("vfs/home/")
        self.assertEqual(self.vfs.current_directory, "/vfs/home/")

    def test_cd_up_one_level(self):
        self.vfs.change_directory("/vfs/home")
        self.vfs.change_directory("..")
        self.assertEqual(self.vfs.current_directory, "/vfs")

    def test_cd_invalid_directory(self):
        with self.assertRaises(FileNotFoundError):
            self.vfs.change_directory("nonexistent")

    def test_ls_root(self):
        output = self.shell.run_command("ls")
        expected = "vfs"
        self.assertEqual(output.strip(), expected.strip())

    def test_ls_documents(self):
        self.shell.run_command("cd /vfs/home/user")
        output = self.shell.run_command("ls")
        expected = "documents\npictures"
        self.assertEqual(output.strip(), expected.strip())

    def test_wc_file(self):
        self.shell.run_command("cd /vfs/home/user/documents")
        result = self.shell.run_command("wc example.txt")
        expected = "[ lines - 3 | words - 18 | chars - 89 | file name - example.txt ]" 
        self.assertEqual(result, expected)

    def test_wc_nonexistent_file(self):
        result = self.shell.run_command("wc nonexistent.txt")
        expected = "[ File nonexistent.txt was not found. ]"
        self.assertEqual(result, expected)

    def test_wc_another_file(self):
        self.shell.run_command("cd /vfs/home/user/documents")
        result = self.shell.run_command("wc report.txt")
        expected = "[ lines - 1 | words - 12 | chars - 67 | file name - report.txt ]"
        self.assertEqual(result, expected)

    def test_du_documents(self):
        self.shell.run_command("cd /vfs/home/user/documents")
        result = self.shell.run_command("du")
        self.assertEqual(result, "156 bytes")
    
    def test_du_pictures(self):
        self.shell.run_command("cd /vfs/home/user/pictures")
        result = self.shell.run_command("du")
        self.assertEqual(result, "0")

    def test_du_root(self):
        result = self.shell.run_command("du")
        self.assertIn("bytes", result)

    def test_exit_shell(self):
        with self.assertRaises(SystemExit):
            self.shell.run_command("exit")

if __name__ == "__main__":
    unittest.main()