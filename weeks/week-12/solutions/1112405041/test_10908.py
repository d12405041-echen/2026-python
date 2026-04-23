import unittest
from io import StringIO
import sys
import importlib

problem_10908 = importlib.import_module("10908")

class TestLargestSquare(unittest.TestCase):
    def test_sample(self):
        input_str = "1\n7 10 4\nabbbaaaaaa\nabbbaaaaaa\nabbbaaaaaa\naaaaaaaaaa\naaaaaaaaaa\naaccaaaaaa\naaccaaaaaa\n1 2\n2 4\n4 6\n5 2\n"
        expected_output = "7 10 4\n3\n1\n5\n1\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10908.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
