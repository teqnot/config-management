import unittest
import main
import zipfile
from unittest.mock import patch, mock_open
import os
import xml.etree.ElementTree as ET

class TestDependencyGraphVisualizer(unittest.TestCase):

    @patch('builtins.open')
    def test_parse_nuspec(self, mock_file):
        deps = main.extract_dependencies("Newtonsoft-Json.nupkg", 5)
        expected = {'.NETStandard1.0': {'Microsoft.CSharp': '4.3.0', 'NETStandard.Library': '1.6.1', 'System.ComponentModel.TypeConverter': '4.3.0', 'System.Runtime.Serialization.Primitives': '4.3.0'}, '.NETStandard1.3': {'Microsoft.CSharp': '4.3.0', 'NETStandard.Library': '1.6.1', 'System.ComponentModel.TypeConverter': '4.3.0', 'System.Runtime.Serialization.Formatters': '4.3.0', 'System.Runtime.Serialization.Primitives': '4.3.0', 'System.Xml.XmlDocument': '4.3.0'}}
        self.assertEqual(deps, expected)

    @patch('zipfile.ZipFile')
    def test_extract_dependencies(self, mock_zip):
        mock_zip.return_value.__enter__.return_value.namelist.return_value = ['package.nuspec']
        mock_zip.return_value.__enter__.return_value.open.return_value = mock_open(read_data='<package></package>').return_value
        
        result = main.extract_dependencies('fake_package.nupkg', 3)
        expected = {}
        self.assertEqual(result, expected)

    def test_parse_dependencies(self):
        deps = [
            ('A', '1.0.0', 'netstandard2.0'),
            ('B', '2.0.0', 'netstandard2.0'),
            ('C', '3.0.0', 'netcoreapp3.1')
        ]
        result = main.parse_dependencies(deps)
        expected = {
            'netstandard2.0': {'A': '1.0.0', 'B': '2.0.0'},
            'netcoreapp3.1': {'C': '3.0.0'}
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
