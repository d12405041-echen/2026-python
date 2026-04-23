import unittest
from io import StringIO
import sys
import importlib

# 更新為符合魔改後的「鏡子可見性」題目要求
problem_11332 = importlib.import_module("11332")

class TestMirrorVisibility(unittest.TestCase):
    def test_sample(self):
        # 1 個鏡子，座標 (1,1) 到 (2,2)
        input_str = "1\n1 1 2 2\n0\n"
        expected_output = "1\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_11332.solve()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
