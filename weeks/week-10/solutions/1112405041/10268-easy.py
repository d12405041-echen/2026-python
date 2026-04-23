import sys

# 【August 的惡意：身分置換 - 簡單版】
# 魔改題目：丟雞蛋 (k 個蛋, n 層樓)
# 此版本簡化了動態規劃，改用更易記憶的組合數邏輯。

def solve():
    def get_f(t, k):
        """t 次嘗試 k 個蛋能確定的最高樓層數 f(t, k) = sum_{i=1}^k C(t, i)"""
        total, term = 0, 1
        for i in range(1, k + 1):
            term = term * (t - i + 1) // i
            total += term
            if total >= (1 << 64): return total
        return total

    # 讀取輸入
    lines = sys.stdin.read().split()
    for i in range(0, len(lines), 2):
        k, n = int(lines[i]), int(lines[i+1])
        if k == 0: break

        found = False
        for t in range(1, 64):
            if get_f(t, k) >= n:
                print(t)
                found = True
                break
        if not found:
            print("More than 63 trials needed.")

if __name__ == "__main__":
    solve()
