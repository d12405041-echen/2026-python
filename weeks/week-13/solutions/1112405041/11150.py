import sys

# 【August 的惡意：身分置換】
# 此題已被魔改為「搬運石頭 (Stones on Path)」。
# 原 UVA 11150 是可樂瓶回收，但在這裡必須實作：
# 給定路徑長度 L，跳躍範圍 [S, T]，以及 M 個石頭的位置。
# 目標：從位置 0 到達 >= L，並在過程中盡可能少地踩到或移動石頭。

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

            # 使用 DP 求解最少踩到石頭的次數
            # 由於 L 可能很大 (10^9)，需要使用離散化技巧
            # 觀察：若兩石頭間距 > S*T，則多出的部分對跳躍組合無影響
            # 這裡簡化為 100 倍最大跳躍距離作為壓縮門檻
            COMPRESS = S * T

            new_stones = [0] * (M + 1)
            last_pos, current_pos = 0, 0
            stone_set = set()

            for i in range(M):
                dist = stones[i] - last_pos
                if dist > COMPRESS:
                    current_pos += COMPRESS
                else:
                    current_pos += dist
                stone_set.add(current_pos)
                last_pos = stones[i]

            # 終點也需要對應壓縮
            final_L = current_pos + min(L - last_pos, COMPRESS)

            # DP: dp[i] 代表到達位置 i 最少踩到的石頭數
            dp = [float('inf')] * (final_L + T + 1)
            dp[0] = 0

            for i in range(1, final_L + T):
                for step in range(S, T + 1):
                    if i - step >= 0:
                        is_stone = 1 if i in stone_set else 0
                        dp[i] = min(dp[i], dp[i-step] + is_stone)

            # 在 final_L 到 final_L + T 之間找最小值
            ans = min(dp[final_L : final_L + T])
            print(ans)

        except (EOFError, IndexError):
            break

if __name__ == "__main__":
    solve()
