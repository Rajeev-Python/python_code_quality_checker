import unittest
from analyzer.suggester import generate_suggestions

class TestSuggester(unittest.TestCase):
    def test_generate_suggestions(self):
        issues = ["E501", "W0611", "R0913"]
        result = generate_suggestions(issues)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

if __name__ == "__main__":
    unittest.main()