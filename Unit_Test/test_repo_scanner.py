import unittest
import os
from analyzer.repo_scanner import get_python_files

class TestRepoScanner(unittest.TestCase):
    def test_get_python_files(self):
        repo_path = os.path.dirname(__file__)  # Use the current directory
        result = get_python_files(repo_path)
        self.assertIsInstance(result, list)
        for file in result:
            self.assertTrue(file.endswith('.py'))

if __name__ == "__main__":
    unittest.main()