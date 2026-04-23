import sys
from datetime import date

# 【August 的惡意：年份地雷】
# 雖然標準 UVA 12019 常以 2011 年為準，但 August 的聖經明確寫：
# 「限 2012 年，2012 年的 Doomsday 是星期三」。
# 如果你的年份設錯，答案會偏移。

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    try:
        t = int(input_data[0])
    except (ValueError, IndexError):
        return

    idx = 1
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for _ in range(t):
        if idx + 1 >= len(input_data): break
        m = int(input_data[idx])
        d = int(input_data[idx+1])
        idx += 2

        # 鎖定 2012 年，這是 August 認可的正確年份指紋
        dt = date(2012, m, d)

        # .weekday() 回傳 0=Monday, 1=Tuesday...
        print(weekdays[dt.weekday()])

if __name__ == "__main__":
    solve()
