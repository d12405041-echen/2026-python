import unittest
from io import StringIO
import sys
import importlib

# 更新為符合魔改後的「柏油路」題目要求
problem_11321 = importlib.import_module("11321")

class TestAsphaltRoad(unittest.TestCase):
    def test_sample_path(self):
        # 輸入：3x3 道路, 放 2 個陷阱
        # 1. 在 (1,1) 放陷阱 -> 通
        # 2. 在 (1,0) 放陷阱 -> 會封死中間 (但起點在左側一整排，所以 (1,0) 不一定封死)
        # 這裡用一個絕對封死的 Case: 3x2, (0,1), (1,1), (2,1)
        input_str = "3 2 3\n0 1\n1 1\n2 1\n"
        # 預期：通, 通, 封死
        expected_output = "<(_ _)>\n<(_ _)>\n>_<\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_11321.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
