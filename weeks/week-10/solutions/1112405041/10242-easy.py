import sys

# 第四個點 (平行四邊形) - 大一小萌新版
# 題目邏輯：
# 給你兩條邊（四個點，其中有兩個點是重複的，那個點就是頂點）
# 平行四邊形第四點的座標 = (點A + 點B) - 共同點

def main():
    # 讀取輸入的所有數字
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    while idx < len(data):
        # 讀取四個點 (x1, y1), (x2, y2), (x3, y3), (x4, y4)
        x1 = float(data[idx]); y1 = float(data[idx+1])
        x2 = float(data[idx+2]); y2 = float(data[idx+3])
        x3 = float(data[idx+4]); y3 = float(data[idx+5])
        x4 = float(data[idx+6]); y4 = float(data[idx+7])
        idx += 8

        # 找出共同的那一個點
        # 假設兩條邊是 (P1, P2) 和 (P3, P4)
        common_x, common_y = 0.0, 0.0
        other1_x, other1_y = 0.0, 0.0
        other2_x, other2_y = 0.0, 0.0

        if x1 == x3 and y1 == y3:
            common_x, common_y = x1, y1
            other1_x, other1_y = x2, y2
            other2_x, other2_y = x4, y4
        elif x1 == x4 and y1 == y4:
            common_x, common_y = x1, y1
            other1_x, other1_y = x2, y2
            other2_x, other2_y = x3, y3
        elif x2 == x3 and y2 == y3:
            common_x, common_y = x2, y2
            other1_x, other1_y = x1, y1
            other2_x, other2_y = x4, y4
        else: # x2 == x4 and y2 == y4
            common_x, common_y = x2, y2
            other1_x, other1_y = x1, y1
            other2_x, other2_y = x3, y3

        # 計算第四點
        res_x = other1_x + other2_x - common_x
        res_y = other1_y + other2_y - common_y

        # 印出結果，保留三位小數
        print("{:.3f} {:.3f}".format(res_x, res_y))

if __name__ == "__main__":
    main()
