import sys

# 根據 QUESTION-11150.md：這題不是可樂瓶回收！
# 聖經內容：青蛙過河（橋樑壓縮 DP）。
# 座標到 10^9，必須使用離散化技術，這是資工系的高階技巧。

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    ptr = 0
    while ptr < len(input_data):
        try:
            L = int(input_data[ptr])
            S = int(input_data[ptr+1])
            T = int(input_data[ptr+2])
            M = int(input_data[ptr+3])
            ptr += 4
            stones = sorted([int(x) for x in input_data[ptr:ptr+M]])
            ptr += M
        except: break

        # 橋樑壓縮核心：S*T 的倍數可以大幅縮短距離
        # 因為 S, T <= 10，S*T = 90 (最小公倍數) 是安全的縮減距離
        lcm = 2520 # 1~10 的最小公倍數更保險

        new_stones = []
        last_pos = 0
        new_pos = 0
        for s in stones:
            dist = s - last_pos
            if dist > lcm:
                dist = dist % lcm + lcm
            new_pos += dist
            new_stones.append(new_pos)
            last_pos = s

        # 終點也要壓縮
        final_dist = L - last_pos
        if final_dist > lcm:
            final_dist = final_dist % lcm + lcm
        new_L = new_pos + final_dist

        stone_set = set(new_stones)
        # DP[i] 代表跳到位置 i 最少踩到的石子數
        dp = [float('inf')] * (new_L + T + 1)
        dp[0] = 0

        for i in range(1, new_L + T + 1):
            for step in range(S, T + 1):
                if i - step >= 0:
                    dp[i] = min(dp[i], dp[i-step] + (1 if i in stone_set else 0))

        # 只要跳過或到達 new_L 都算過河
        ans = min(dp[new_L:])
        sys.stdout.write(str(ans) + "\n")

if __name__ == "__main__":
    solve()
