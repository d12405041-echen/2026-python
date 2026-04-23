import unittest
from io import StringIO
import sys
import importlib

problem_10226 = importlib.import_module("10226")

class TestSpecies(unittest.TestCase):
    def test_sample(self):
        # 2人 A, B.
        # A 不想排 1. (限制: A 只能排 2)
        # B 不想排 2. (限制: B 只能排 1)
        # 唯一可能: BA
        input_str = "2\n1 0\n2 0\n"
        expected_output = "BA\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10226.solve()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
