import sys

# 根據 QUESTION-10783.md：這題不是 Odd Sum！
# 聖經內容：字母排列 (Letters) - 尋找最長照順序排列的子字串。
# 規則：abcwkodvwxyzwia -> abc (3), vwxyz (5) -> 最後出現的最長子字串。

def solve():
    raw = sys.stdin.read().strip()
    if not raw: return

    # 只要小寫字母
    s = "".join([c for c in raw if c.islower()])
    if not s: return

    n = len(s)
    max_len = 1
    best_str = s[0]

    curr_len = 1
    for i in range(1, n):
        # 檢查是否照字母順序 (A -> B -> C)
        if ord(s[i]) == ord(s[i-1]) + 1:
            curr_len += 1
        else:
            curr_len = 1

        if curr_len >= max_len:
            max_len = curr_len
            best_str = s[i - curr_len + 1 : i + 1]

    sys.stdout.write(f"{max_len}{best_str}")

if __name__ == "__main__":
    solve()
