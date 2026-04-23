import unittest
from io import StringIO
import sys
import importlib

problem_11005 = importlib.import_module("11005")

class TestCheapestBase(unittest.TestCase):
    def test_sample(self):
        # 簡單測試: 如果所有成本都是 1, 那所有進位制成本都一樣
        # 但數字 10 在 11 進位以上就只剩下一位數, 所以成本會是 costs[10]
        # 在 10 進位以下是多位數, 成本會更高.
        # 所以只有 11~36 進位才是最便宜的.
        costs = "1 " * 36
        input_str = "1\n" + costs + "1\n10\n"
        expected_output = "Case 1:\nCheapest base(s) for number 10: 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_11005.solve()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
