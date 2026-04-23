import sys

# 超級盃比分計算 (Beat the Spread!) - 大一小萌新版
# 題目邏輯：
# 給你兩隊分數的和 (S) 和 差 (D)，求兩隊各得幾分。
# 公式： 較高分 = (S + D) / 2, 較低分 = (S - D) / 2
# 條件： S+D 必須是偶數，而且 S 不能小於 D (不然會有負分)。

def main():
    # 讀取輸入
    input_text = sys.stdin.read().split()
    if not input_text:
        return

    # 第一行是組數
    num_cases = int(input_text[0])

    idx = 1
    for i in range(num_cases):
        # 讀取和 S 與 差 D
        s = int(input_text[idx])
        d = int(input_text[idx+1])
        idx += 2

        # 1. 判斷有沒有可能：
        # 如果 和 小於 差，這是不可能的 (會出現負數分數)
        # 如果 和 + 差 不是偶數，那就沒辦法除盡 (題目要求整數得分)
        if s < d or (s + d) % 2 != 0:
            print("impossible")
        else:
            # 2. 計算比分
            team1 = (s + d) // 2
            team2 = (s - d) // 2
            # 題目要求大的先輸出
            print(str(team1) + " " + str(team2))

if __name__ == "__main__":
    main()
