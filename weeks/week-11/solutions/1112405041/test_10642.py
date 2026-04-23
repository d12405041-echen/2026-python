import unittest
from io import StringIO
import sys
import importlib

problem_10642 = importlib.import_module("10642")

class TestCanYouSolveIt(unittest.TestCase):
    def test_sample(self):
        # (0,0) seq=0, (0,1) seq=1, (1,0) seq=2, (0,2) seq=3
        # 0 0 0 1 -> Case 1: 1
        # 0 0 1 0 -> Case 2: 2
        # 0 0 0 2 -> Case 3: 3
        input_str = "3\n0 0 0 1\n0 0 1 0\n0 0 0 2\n"
        expected_output = "Case 1: 1\nCase 2: 2\nCase 3: 3\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10642.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
