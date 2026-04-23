import sys

# 路徑步數計算 (Can You Solve It?) - 大一小萌新版
# 題目邏輯：
# 想像一張地圖，節點是按照斜線排列的：
# 斜線 0: (0,0)
# 斜線 1: (0,1), (1,0)
# 斜線 2: (0,2), (1,1), (2,0)
# 我們只要算出每個點在整個序列中的「序號」，兩個點的序號相減就是步數。

def get_sequence_number(x, y):
    # s 是這點所在的斜線編號 (x+y)
    line_sum = x + y

    # 算出在這一條斜線之前的斜線總共有多少個點
    # 第 0 條有 1 個，第 1 條有 2 個... 到第 line_sum - 1 條
    # 總數公式是 (1 + line_sum) * line_sum / 2
    count_before = (line_sum * (line_sum + 1)) // 2

    # 在目前這條斜線中，這點是第幾個
    # 依照規則，(0, line_sum) 是第一個，(1, line_sum-1) 是第二個...
    # 所以 (x, y) 就是第 x + 1 個
    current_line_pos = x

    return count_before + current_line_pos

def main():
    # 讀取輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # 第一個數字是測試組數
    num_cases = int(input_data[0])

    idx = 1
    for i in range(1, num_cases + 1):
        # 每組有四個數字：x1, y1, x2, y2
        x1 = int(input_data[idx])
        y1 = int(input_data[idx+1])
        x2 = int(input_data[idx+2])
        y2 = int(input_data[idx+3])
        idx += 4

        # 算出起點和終點的序號
        start_pos = get_sequence_number(x1, y1)
        end_pos = get_sequence_number(x2, y2)

        # 步數就是兩者的差
        steps = end_pos - start_pos

        # 按格式印出結果
        print("Case " + str(i) + ": " + str(steps))

if __name__ == "__main__":
    main()
