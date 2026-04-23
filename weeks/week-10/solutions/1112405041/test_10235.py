import unittest
from io import StringIO
import sys
import importlib

problem_10235 = importlib.import_module("10235")

class TestEmirp(unittest.TestCase):
    def test_cases(self):
        # 17 -> 71 (both prime) -> emirp
        # 13 -> 31 (both prime) -> emirp
        # 19 -> 91 (91=7*13) -> prime
        # 7 -> 7 (same) -> prime
        input_str = "17\n13\n19\n7\n"
        expected_output = "17 is emirp.\n13 is emirp.\n19 is prime.\n7 is prime.\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10235.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
