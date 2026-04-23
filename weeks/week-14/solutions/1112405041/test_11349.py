import unittest
from io import StringIO
import sys
import importlib

problem_11349 = importlib.import_module("11349")

class TestSymmetricMatrix(unittest.TestCase):
    def test_sample(self):
        # N = 2, values: 5 1 1 5 -> Symmetric
        input_str = "1\nN = 2\n5 1\n1 5\n"
        expected_output = "Test #1: Symmetric.\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_11349.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
