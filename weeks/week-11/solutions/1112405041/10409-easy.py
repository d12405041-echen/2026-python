import sys

# 骰子遊戲 (Die Game) - 大一小萌新入門版
# 我們要模擬一顆骰子在桌面上滾來滾去。
# 骰子的規則：相對面的數字加起來一定是 7 (例如頂面是 1，底面就是 6)。

def main():
    # 讀取所有的指令
    input_lines = sys.stdin.readlines()
    line_ptr = 0

    while line_ptr < len(input_lines):
        # 讀取這一輪有多少個動作
        n_str = input_lines[line_ptr].strip()
        if not n_str:
            line_ptr += 1
            continue
        n = int(n_str)
        line_ptr += 1

        # 如果 n 是 0，代表遊戲結束了
        if n == 0:
            break

        # 設定初始狀態
        # 我們只需要追蹤「頂面 (top)」、「北面 (north)」和「西面 (west)」
        # 剩下的南面、東面、底面都可以用 (7 - 相對面) 算出來
        top = 1
        north = 2
        west = 3

        for i in range(n):
            command = input_lines[line_ptr].strip()
            line_ptr += 1

            # 根據不同方向翻轉骰子
            if command == "north":
                # 往北翻：
                # 原本的南面變頂面 (南面 = 7 - 北面)
                # 原本的頂面變北面
                # 西面維持不變
                new_top = 7 - north
                new_north = top
                top = new_top
                north = new_north

            elif command == "south":
                # 往南翻：
                # 原本的北面變頂面
                # 原本的頂面變南面 (南面 = 7 - 北面，所以新北面 = 7 - 原頂面)
                new_top = north
                new_north = 7 - top
                top = new_top
                north = new_north

            elif command == "west":
                # 往西翻：
                # 原本的東面變頂面 (東面 = 7 - 西面)
                # 原本的頂面變西面
                # 北面維持不變
                new_top = 7 - west
                new_west = top
                top = new_top
                west = new_west

            elif command == "east":
                # 往東翻：
                # 原本的西面變頂面
                # 原本的頂面變東面 (東面 = 7 - 西面，所以新西面 = 7 - 原頂面)
                new_top = west
                new_west = 7 - top
                top = new_top
                west = new_west

        # 最後印出最上面的數字
        print(top)

if __name__ == "__main__":
    main()
