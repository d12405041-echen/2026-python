import sys

# 完全平方數計數 (Square Numbers) - 大一小萌新版
# 題目邏輯：
# 給你一個範圍 [a, b]，算出這中間有多少個完全平方數 (例如 1, 4, 9, 16...)。
# 技巧：不需要一個一個檢查，只要算 sqrt(a) 和 sqrt(b) 之間的整數個數就可以了。

def main():
    # 讀取輸入
    input_text = sys.stdin.read().split()
    if not input_text:
        return

    idx = 0
    while idx < len(input_text):
        a = int(input_text[idx])
        b = int(input_text[idx + 1])
        idx += 2

        # 0 0 代表結束
        if a == 0 and b == 0:
            break

        # 找出第一個平方後會大於等於 a 的整數
        # 使用開根號的方式
        import math
        # math.ceil 是無條件進位
        start_root = int(math.ceil(math.sqrt(a)))

        # 找出最後一個平方後會小於等於 b 的整數
        # math.floor 是無條件捨去
        end_root = int(math.floor(math.sqrt(b)))

        # 如果範圍正確，個數就是 end - start + 1
        if start_root > end_root:
            print(0)
        else:
            print(end_root - start_root + 1)

if __name__ == "__main__":
    main()
