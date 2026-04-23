import sys

# 最大正方形 (Largest Square) - 大一小萌新版
# 題目邏輯：
# 給你一個中心點 (r, c)，我們要檢查以它為中心，往外擴張的正方形是否所有字元都一樣。
# 邊長必須是奇數 (1, 3, 5...)。
# 我們就從邊長 1 開始，每次往外加一圈 (邊長變成 3, 5, 7...) 檢查，直到撞到邊界或字元不同。

def main():
    # 讀取輸入
    input_text = sys.stdin.read().split()
    if not input_text:
        return

    # T 是測試資料筆數
    t = int(input_text[0])
    idx = 1

    for _ in range(t):
        # M: 行數, N: 列數, Q: 查詢次數
        m = int(input_text[idx])
        n = int(input_text[idx+1])
        q = int(input_text[idx+2])
        idx += 3

        # 輸出網格資訊
        print(str(m) + " " + str(n) + " " + str(q))

        # 讀取網格字元
        grid = input_text[idx:idx+m]
        idx += m

        for _ in range(q):
            # 讀取查詢的中心座標 (r, c)
            center_r = int(input_text[idx])
            center_c = int(input_text[idx+1])
            idx += 2

            # 中心點的字元是什麼
            target_char = grid[center_r][center_c]

            # 初始邊長是 1
            max_side = 1

            # 嘗試往外擴張一圈 (新的半徑 k)
            # 邊長 1 對應 k=0, 邊長 3 對應 k=1, 邊長 5 對應 k=2
            k = 1
            while True:
                # 正方形的邊界
                top = center_r - k
                bottom = center_r + k
                left = center_c - k
                right = center_c + k

                # 檢查是否超出網格邊界
                if top < 0 or bottom >= m or left < 0 or right >= n:
                    break

                # 檢查這一圈的所有字元是否都符合
                is_valid = True
                for r in range(top, bottom + 1):
                    for c in range(left, right + 1):
                        if grid[r][c] != target_char:
                            is_valid = False
                            break
                    if not is_valid:
                        break

                if is_valid:
                    # 這一圈都對，邊長增加 (2*k + 1)
                    max_side = 2 * k + 1
                    k += 1 # 準備看下一圈
                else:
                    # 只要有一個字元不對，就停止擴張
                    break

            # 印出這組查詢的最大邊長
            print(max_side)

if __name__ == "__main__":
    main()
