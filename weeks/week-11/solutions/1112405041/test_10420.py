import unittest
from io import StringIO
import sys
import importlib

problem_10420 = importlib.import_module("10420")

class TestConquests(unittest.TestCase):
    def test_sample(self):
        input_str = "3\nSpain Donna Elvira\nEngland Jane Doe\nSpain Donna Anna\n"
        expected_output = "England 1\nSpain 2\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10420.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
