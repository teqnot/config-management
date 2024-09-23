import unittest
import zipfile
import os
from io import BytesIO
from shell import ShellEmulator
from filesystem import VirtualFileSystem

class TestVirtualFileSystem(unittest.TestCase):

    def setUp(self):
        self.test_zip_data = "vfs2.zip"
        self.shell = ShellEmulator("user", "host", self.test_zip_data)
        self.vfs = VirtualFileSystem(self.test_zip_data)

    def test_cd_root(self):
        self.shell.run_command("cd /")
        self.assertEqual(self.vfs.get_current_directory, "/")

    def test_cd_home(self):
        self.shell.run_command("cd vfs/home")
        self.assertEqual(self.vfs.get_current_directory, "/vfs/home")

    def test_cd_up_one_level(self):
        self.shell.run_command("cd /vfs/home")
        self.shell.run_command("cd ..")
        self.assertEqual(self.vfs.get_current_directory, "/vfs")

    def test_cd_invalid_directory(self):
        with self.assertRaises(FileNotFoundError):
            self.shell.run_command("cd nonexistent")

    def test_ls_root(self):
        output = self.shell.run_command("ls")
        expected = "vfs"
        self.assertEqual(output.strip(), expected.strip())

    def test_ls_documents(self):
        self.shell.run_command("cd /vfs/home")
        output = self.shell.run_command("ls")
        expected = "\ndocuments"
        self.assertEqual(output.strip(), expected.strip())

    def test_wc_file(self):
        self.shell.run_command("cd /vfs/home/user/documents")
        result = self.shell.run_command("wc example.txt")
        expected = "[ 2 7 35 test.txt ]"  # 2 lines, 7 words, 35 characters
        self.assertEqual(result, expected)

    def test_wc_nonexistent_file(self):
        self.shell.run_command("cd documents")
        with self.assertRaises(FileNotFoundError):
            self.shell.run_command("wc nonexistent.txt")

    def test_du_current_directory(self):
        self.shell.run_command("cd documents")
        result = self.shell.run_command("du")
        self.assertIn("bytes", result)

    def test_du_root(self):
        result = self.shell.run_command("du")
        self.assertIn("bytes", result)

    def test_exit_shell(self):
        with self.assertRaises(SystemExit):
            self.shell.run_command("exit")

if __name__ == "__main__":
    unittest.main()