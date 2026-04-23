import sys

# 青蛙過河 (橋樑壓縮 DP) - 大一小萌新簡單版
# 雖然題目編號是 11150，但讀完 .md 就知道這絕對不是可樂瓶回收！
# 💡 核心邏輯：橋太長了 (10^9)，所以我們要用「壓縮」的方法，
# 把石頭之間太遠的距離縮短到我們處理得了的範圍。

def main():
    # 讀取輸入資料
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    ptr = 0
    while ptr < len(input_data):
        # L: 橋長, S~T: 跳躍距離, M: 石頭數量
        L = int(input_data[ptr])
        S = int(input_data[ptr+1])
        T = int(input_data[ptr+2])
        M = int(input_data[ptr+3])
        ptr += 4

        # 石頭的位置並排序
        stones = []
        for i in range(M):
            stones.append(int(input_data[ptr]))
            ptr += 1
        stones.sort()

        # 這裡用一個資工系的大絕招：距離壓縮 (LCM 技巧)
        # 因為跳躍範圍最大才 10，1 到 10 的最小公倍數是 2520。
        # 只要兩個石頭中間距離超過 2520，我們就可以把它縮短成 2520 以內的距離。
        lcm = 2520

        compressed_stones = []
        last_pos = 0
        new_pos = 0
        for s in stones:
            dist = s - last_pos
            if dist > lcm:
                # 距離太長了，壓縮它！
                dist = (dist % lcm) + lcm
            new_pos += dist
            compressed_stones.append(new_pos)
            last_pos = s

        # 終點也要跟著壓縮
        final_dist = L - last_pos
        if final_dist > lcm:
            final_dist = (final_dist % lcm) + lcm
        new_L = new_pos + final_dist

        # 用集合來記錄哪些位置有石頭，這樣查起來很快
        stone_set = set(compressed_stones)

        # 建立 DP 陣列，DP[i] 代表跳到位置 i 時，「最少」會踩到幾個石頭
        # 一開始我們設為無限大
        dp = [999999] * (new_L + T + 1)
        dp[0] = 0 # 起點沒石頭，踩到 0 個

        # 開始跳跳跳！
        for i in range(1, new_L + T + 1):
            for step in range(S, T + 1):
                prev = i - step
                if prev >= 0:
                    # 看看從 prev 跳過來會踩到幾顆
                    current_cost = dp[prev]
                    if i in stone_set:
                        current_cost += 1

                    if current_cost < dp[i]:
                        dp[i] = current_cost

        # 只要跳到大於或等於 new_L 的地方，就算過河了
        # 我們找出這些位置中，石頭最少的那一個
        ans = min(dp[new_L : new_L + T + 1])
        print(ans)

if __name__ == "__main__":
    main()
