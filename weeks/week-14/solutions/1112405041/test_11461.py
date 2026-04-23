import unittest
from io import StringIO
import sys
import importlib

problem_11461 = importlib.import_module("11461")

class TestSquareNumbers(unittest.TestCase):
    def test_sample(self):
        # [1, 4] -> 1, 4 -> 2
        # [1, 10] -> 1, 4, 9 -> 3
        input_str = "1 4\n1 10\n0 0\n"
        expected_output = "2\n3\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_11461.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
