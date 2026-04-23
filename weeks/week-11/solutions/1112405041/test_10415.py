import unittest
from io import StringIO
import sys
import importlib

problem_10415 = importlib.import_module("10415")

class TestSaxophone(unittest.TestCase):
    def test_sample(self):
        # 輸入旋律 "cde"
        # c: [2,3,4,7,8,9,10]
        # d: [2,3,4,7,8,9] -> 沒增加
        # e: [2,3,4,7,8] -> 沒增加
        # 結果: 0 1 1 1 0 0 1 1 1 1
        input_str = "1\ncde\n"
        expected_output = "0 1 1 1 0 0 1 1 1 1\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10415.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
