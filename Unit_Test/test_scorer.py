import unittest
from analyzer.scorer import calculate_file_score

class TestScorer(unittest.TestCase):
    def test_calculate_file_score(self):
        linter_issues = ["E501", "W0611"]
        complexity_metrics = {"complexity_score": 80}
        result = calculate_file_score(linter_issues, complexity_metrics)
        self.assertIn('complexity_score', result)
        self.assertIn('total_score', result)
        self.assertGreaterEqual(result['total_score'], 0)

if __name__ == "__main__":
    unittest.main()