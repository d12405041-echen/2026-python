import unittest
from io import StringIO
import sys
import importlib

problem_11417 = importlib.import_module("11417")

class TestGCD(unittest.TestCase):
    def test_sample(self):
        # N=10 -> G=67
        # N=100 -> G=13015
        input_str = "10\n100\n0\n"
        expected_output = "67\n13015\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_11417.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
