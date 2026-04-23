import sys

# 【August 的惡意：身分置換 - 簡單版】
# 魔改題目：磁磚覆蓋問題 (N x M 網格)
# 此版本使用遞迴 + 記憶化，比起輪廓線 DP 更容易理解與撰寫。

memo = {}

def count_ways(r, c, mask, n, m, grid):
    state = (r, c, mask)
    if state in memo: return memo[state]
    if r == n: return 1 if mask == 0 else 0

    # 下一個格子的位置
    nr, nc = (r, c + 1) if c + 1 < m else (r + 1, 0)

    res = 0
    # 如果當前格子已被覆蓋或為障礙物，直接跳到下一格
    if (mask & 1) or grid[r][c] == 0:
        res = count_ways(nr, nc, mask >> 1, n, m, grid)
    else:
        # 1. 嘗試垂直放 (向下伸)
        if r + 1 < n and grid[r+1][c] == 1:
            res = (res + count_ways(nr, nc, (mask >> 1) | (1 << (m - 1)), n, m, grid)) % 1000000007
        # 2. 嘗試水平放 (向右伸)
        if c + 1 < m and grid[r][c+1] == 1 and not (mask & 2):
            res = (res + count_ways(r, c + 2, mask >> 2, n, m, grid) if c + 2 < m else count_ways(r + 1, 0, mask >> 2, n, m, grid)) % 1000000007

    memo[state] = res
    return res

def solve():
    # 簡單版主邏輯
    pass # 這裡省略繁瑣輸入，核心邏輯見 count_ways
