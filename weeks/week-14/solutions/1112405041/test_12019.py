import unittest
from io import StringIO
import sys
import importlib

problem_12019 = importlib.import_module("12019")

class TestDoomsDay(unittest.TestCase):
    def test_sample(self):
        # 2011/1/6 -> Thursday
        # 2011/2/13 -> Sunday
        input_str = "2\n1 6\n2 13\n"
        expected_output = "Thursday\nSunday\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_12019.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
