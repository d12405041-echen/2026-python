import unittest
from io import StringIO
import sys
import importlib

problem_10929 = importlib.import_module("10929")

class TestCheck11s(unittest.TestCase):
    def test_sample(self):
        # 112233 -> 1-1+2-2+3-3=0 (multiple)
        # 308 -> 3-0+8=11 (multiple)
        # 2937 -> 2-9+3-7=-11 (multiple)
        input_str = "112233\n308\n2937\n323456\n0\n"
        expected_output = "112233 is a multiple of 11.\n308 is a multiple of 11.\n2937 is a multiple of 11.\n323456 is not a multiple of 11.\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10929.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
