# 948.py
# UVA 948：Fibonaccimal Base
# 功能：將整數轉換為斐波那契進位表示法 (Zeckendorf's Theorem)

import sys

class FibonaccimalConverter:
    def __init__(self, limit: int = 100000000):
        # 預先計算斐波那契數列，直到超過上限
        self.fibs = [1, 2]
        while self.fibs[-1] < limit:
            self.fibs.append(self.fibs[-1] + self.fibs[-2])
        # 我們需要從大到小遍歷，所以反轉或使用索引
        self.fibs.reverse()

    def convert(self, n: int) -> str:
        """根據齊肯多夫定理，任何正整數都能唯一表示為不連續斐波那契數之和。"""
        if n == 0:
            return "0 (fib)"

        temp_n = n
        result = []
        started = False

        for f in self.fibs:
            if temp_n >= f:
                result.append("1")
                temp_n -= f
                started = True
            elif started:
                result.append("0")

        return f"{n} = {''.join(result)} (fib)"

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n_cases = int(input_data[0])
    converter = FibonaccimalConverter()

    for i in range(1, n_cases + 1):
        num = int(input_data[i])
        print(converter.convert(num))

if __name__ == "__main__":
    main()
