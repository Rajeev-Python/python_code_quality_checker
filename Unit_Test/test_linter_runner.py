import unittest
from analyzer.linter_runner import run_flake8, run_pylint

class TestLinterRunner(unittest.TestCase):
    def test_run_flake8(self):
        result = run_flake8(__file__)  # Test the current file
        self.assertIsInstance(result, list)

    def test_run_pylint(self):
        result = run_pylint(__file__)  # Test the current file
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()