import unittest
from io import StringIO
import sys
import importlib

problem_10812 = importlib.import_module("10812")

class TestBeatTheSpread(unittest.TestCase):
    def test_cases(self):
        # 40 20 -> 30 10
        # 20 40 -> impossible
        input_str = "2\n40 20\n20 40\n"
        expected_output = "30 10\nimpossible\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10812.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
