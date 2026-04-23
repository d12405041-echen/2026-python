import sys
from datetime import date

# 2011 誰是星期幾 (Doom’s Day Algorithm / 2011-m-d) - 大一小萌新版
# 題目邏輯：
# 給你 2011 年的某月某日，算出那天是星期幾。
# 技巧：直接用 Python 內建的 datetime 模組來算最快也最準。

def main():
    # 建立一個星期名稱的清單，對應 datetime 的 index (0 是 Monday, 6 是 Sunday)
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # 讀取輸入
    input_text = sys.stdin.read().split()
    if not input_text:
        return

    # 測試組數
    num_cases = int(input_text[0])
    idx = 1

    for i in range(num_cases):
        month = int(input_text[idx])
        day = int(input_text[idx + 1])
        idx += 2

        # 使用 Python 內建的 date 物件
        # 建立 2011 年對應月份與日期的物件
        target_date = date(2011, month, day)

        # 取得星期幾的 index (0-6)
        day_of_week_index = target_date.weekday()

        # 輸出對應的英文名稱
        print(weekdays[day_of_week_index])

if __name__ == "__main__":
    main()
