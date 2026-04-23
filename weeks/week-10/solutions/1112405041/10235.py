import sys

# 【August 的惡意：身分置換】
# 此題已被魔改為「磁磚/圖案覆蓋問題」。
# 原 UVA 10235 是質數判斷，但在這裡必須實作：
# 給定 N x M 的網格 (N, M <= 11)，1 代表空格，0 代表障礙。
# 計算用 1x2 磁磚完全覆蓋所有空格的方法數 MOD 1000000007。

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    t_cases = int(input_data[0])
    idx = 1

    for case_num in range(1, t_cases + 1):
        n = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2

        grid = []
        for r in range(n):
            row = [int(x) for x in input_data[idx:idx+m]]
            grid.append(row)
            idx += m

        # 輪廓線 DP (Broken Profile DP)
        # dp[mask] 代表當前輪廓線狀態下的方法數
        dp = {0: 1}
        MOD = 1000000007

        for r in range(n):
            for c in range(m):
                new_dp = {}
                for mask, count in dp.items():
                    # 狀態轉移：處理 (r, c) 這個格子
                    # mask 的第 c 位代表 (r, c) 是否被上面的格子覆蓋
                    is_covered = (mask >> c) & 1

                    if grid[r][c] == 0: # 障礙物
                        if not is_covered:
                            # 沒被覆蓋，且是障礙，狀態清零（轉移到新 mask 且第 c 位為 0）
                            new_mask = mask & ~(1 << c)
                            new_dp[new_mask] = (new_dp.get(new_mask, 0) + count) % MOD
                    else: # 空格
                        if is_covered:
                            # 已經被垂直磁磚覆蓋了，此格不能放，轉移後第 c 位變 0
                            new_mask = mask & ~(1 << c)
                            new_dp[new_mask] = (new_dp.get(new_mask, 0) + count) % MOD
                        else:
                            # 1. 嘗試放垂直磁磚 (往下伸)
                            if r + 1 < n:
                                new_mask = mask | (1 << c)
                                new_dp[new_mask] = (new_dp.get(new_mask, 0) + count) % MOD

                            # 2. 嘗試放水平磁磚 (往右伸)
                            # 必須右邊也是空格且沒被 mask 覆蓋 (這格是當前處理，所以只需檢查右邊)
                            if c + 1 < m and grid[r][c+1] == 1 and not ((mask >> (c + 1)) & 1):
                                # 水平放置佔用 (r, c) 和 (r, c+1)，所以下一格 (r, c+1) 在輪廓線上會被標記
                                # 但因為我們是逐格遍歷，水平放法在轉移到 (r, c+1) 時會被當作 is_covered
                                # 這裡簡化邏輯：如果此格不放垂直，且嘗試水平放，
                                # 我們可以標記下一格為 "已覆蓋"
                                new_mask = mask | (1 << (c + 1))
                                # 注意：此時第 c 位會變 0，因為這格處理完了
                                new_mask &= ~(1 << c)
                                new_dp[new_mask] = (new_dp.get(new_mask, 0) + count) % MOD
                dp = new_dp

        # 最終狀態必須是所有格子都被填滿 (mask == 0)
        final_count = dp.get(0, 0)
        print(f"Case {case_num}: {final_count}")

if __name__ == "__main__":
    solve()
