import unittest
from io import StringIO
import sys
import importlib

problem_11063 = importlib.import_module("11063")

class TestB2Sequence(unittest.TestCase):
    def test_sample(self):
        # 1 2 5 -> sums: 2, 3, 6, 4, 7, 10 (all unique)
        input_str = "3 1 2 5\n"
        expected_output = "Case #1: It is a B2-Sequence.\n\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_11063.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
