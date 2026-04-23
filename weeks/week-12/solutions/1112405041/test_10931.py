import unittest
from io import StringIO
import sys
import importlib

problem_10931 = importlib.import_module("10931")

class TestParity(unittest.TestCase):
    def test_sample(self):
        input_str = "1\n2\n10\n21\n0\n"
        expected_output = "The parity of 1 is 1 (mod 2).\nThe parity of 10 is 1 (mod 2).\nThe parity of 1010 is 2 (mod 2).\nThe parity of 10101 is 3 (mod 2).\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10931.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
