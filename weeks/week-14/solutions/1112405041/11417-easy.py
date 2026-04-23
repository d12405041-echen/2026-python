import sys

# 最大公因數總和 (GCD) - 大一小萌新版
# 題目邏輯：
# 給你一個數字 N，我們要算出從 1 到 N 之間，所有可能的組合 (i, j) 的最大公因數 (GCD) 總和。
# 其中 i < j。

def get_gcd(a, b):
    # 使用輾轉相除法算出最大公因數
    while b != 0:
        a, b = b, a % b
    return a

def main():
    # 讀取輸入
    for line in sys.stdin:
        line = line.strip()
        if not line or line == "0":
            break

        n = int(line)
        total_gcd_sum = 0

        # 雙層迴圈跑遍所有 i < j 的組合
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                # 累加每一組的 GCD
                total_gcd_sum += get_gcd(i, j)

        # 印出最後的總和
        print(total_gcd_sum)

if __name__ == "__main__":
    main()
