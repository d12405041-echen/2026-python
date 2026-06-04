"""UVA 11417 GCD — 測試案例

題目：sum_of_gcd(n) 計算 1 <= i < j <= n 範圍內所有 gcd(i, j) 的總和。
"""

import unittest

# 紅燈階段：匯入預期會失敗，因為 gcd.py 還沒寫
try:
    from gcd import sum_of_gcd
except ImportError:
    sum_of_gcd = None


class TestSumOfGcd(unittest.TestCase):
    def test_n_equals_2(self):
        # gcd(1,2) = 1，總和應為 1
        self.assertEqual(sum_of_gcd(2), 1)

    def test_n_equals_10(self):
        # 範例答案 67
        self.assertEqual(sum_of_gcd(10), 67)

    def test_edge_case_n1(self):
        # n=1 時應為 0
        self.assertEqual(sum_of_gcd(1), 0)


if __name__ == "__main__":
    unittest.main()
