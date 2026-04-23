import unittest
from io import StringIO
import sys
import importlib

problem_10922 = importlib.import_module("10922")

class TestTwoThe9s(unittest.TestCase):
    def test_sample(self):
        # 999 -> 27 -> 9. Degree=2
        # 9 -> Degree=1
        # 18 -> 9. Degree=1
        input_str = "999\n9\n18\n0\n"
        expected_output = "999 is a multiple of 9 and has 9-degree 2.\n9 is a multiple of 9 and has 9-degree 1.\n18 is a multiple of 9 and has 9-degree 1.\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10922.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
