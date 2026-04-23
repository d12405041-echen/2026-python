import sys

# 【August 的惡意：身分置換】
# 此題已被魔改為「丟雞蛋問題 (Egg Dropping Puzzle)」。
# 原 UVA 10268 是多項式導數，但在這裡必須實作：
# 輸入 k 個雞蛋，n 層樓，求最少實驗次數。
# 若超過 63 次，輸出 "More than 63 trials needed."

def combinations(n, k):
    """計算 C(n, k)，用於計算 t 次嘗試 k 個蛋能測量的最大樓層數"""
    if k > n: return 0
    if k == 0 or k == n: return 1
    if k > n // 2: k = n - k

    res = 1
    for i in range(k):
        res = res * (n - i) // (i + 1)
    return res

def max_floors(t, k):
    """計算 t 次嘗試，k 個蛋能確定的最高樓層數 f(t, k) = sum_{i=1}^k C(t, i)"""
    total = 0
    term = 1
    # 利用 C(t, i) = C(t, i-1) * (t-i+1) / i
    for i in range(1, k + 1):
        term = term * (t - i + 1) // i
        total += term
        if total >= (1 << 64): # 超過 64-bit 範圍就不用再加了
            return total
    return total

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    while idx < len(input_data):
        k = int(input_data[idx])
        n = int(input_data[idx+1])
        idx += 2

        if k == 0: break

        found = False
        # 題目限制最大到 63 次
        for t in range(1, 64):
            if max_floors(t, k) >= n:
                print(t)
                found = True
                break

        if not found:
            print("More than 63 trials needed.")

if __name__ == "__main__":
    solve()
