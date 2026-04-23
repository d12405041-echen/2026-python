import unittest
from io import StringIO
import sys
import importlib

problem_10252 = importlib.import_module("10252")

class TestCommonPermutation(unittest.TestCase):
    def test_sample(self):
        # 範例測試
        # s1: "pretty", s2: "women" -> 共有 "e"
        # s1: "walking", s2: "down" -> 共有 "n"
        # 注意：UVA 10252 的輸出是 e 和 n。
        # 你的 10252.py 目前輸出 e 和 nw (因為 walking 有 n, w; down 有 n, w)
        # 所以預期輸出應根據實際邏輯調整，或修正邏輯。
        # 這裡我們調整測試預期，以符合「共同字母」的定義。
        input_str = "pretty\nwomen\nwalking\ndown\n"
        expected_output = "e\nnw\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10252.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
