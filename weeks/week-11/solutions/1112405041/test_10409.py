import unittest
from io import StringIO
import sys
import importlib

problem_10409 = importlib.import_module("10409")

class TestDieGame(unittest.TestCase):
    def test_sample(self):
        # 1 north -> top=5
        # 3 north, east, south -> top=1, north=2, west=3 -> north -> top=5, north=1, west=3 -> east -> top=3, north=1, west=2 -> south -> top=1, north=3, west=2
        input_str = "1\nnorth\n3\nnorth\neast\nsouth\n0\n"
        expected_output = "5\n1\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10409.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
