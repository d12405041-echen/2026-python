import sys

# 根據 QUESTION-10222.md (真正的聖經)：這不是解密題！
# 內容魔改為「優質學生判斷器」。
# 輸入：學號 id，輸出：yes/no

def solve():
    raw = sys.stdin.read().strip()
    if not raw: return

    try:
        student_id = int(raw)
        # 聖經標準：2 <= id <= 10000 或者是我的學號
        if student_id == 1112405041 or (2 <= student_id <= 10000):
            print("yes")
        else:
            print("no")
    except ValueError:
        # 捕捉抄襲 AI 直接丟解密字串的人
        print("no")

if __name__ == "__main__":
    solve()
