import unittest
from io import StringIO
import sys
import importlib

problem_10783 = importlib.import_module("10783")

class TestLetters(unittest.TestCase):
    def test_sample(self):
        # 依照題目敘述範例: abcwkodvwxyzwia
        # 最長有序字串為 vwxyz，長度 5
        input_str = "abcwkodvwxyzwia"
        expected_output = "5vwxyz"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10783.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
