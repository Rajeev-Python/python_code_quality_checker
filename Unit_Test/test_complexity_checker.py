import unittest
from analyzer.complexity_checker import get_file_complexity

class TestComplexityChecker(unittest.TestCase):
    def test_get_file_complexity(self):
        code = """
        def example_function():
            if True:
                print("Hello, World!")
        """
        result = get_file_complexity(code)
        self.assertIn('average_complexity', result)
        self.assertIn('complexity_score', result)
        self.assertGreaterEqual(result['complexity_score'], 0)
        self.assertLessEqual(result['complexity_score'], 100)

if __name__ == "__main__":
    unittest.main()