import sys

# 排隊的小光 - 大一入門版 (DFS 遞迴版)
# 題目要求：N 個人排列，但有些人有不想去的位置。
# 我們要用遞迴 (DFS) 找出所有可能，並只印出跟前一次不同的部分。

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    ptr = 0
    while ptr < len(input_data):
        n = int(input_data[ptr])
        ptr += 1

        # 讀取每個人不想去的位置 (1-based)
        disallowed = []
        for i in range(n):
            bad_pos = []
            while True:
                val = int(input_data[ptr])
                ptr += 1
                if val == 0: break
                bad_pos.append(val)
            disallowed.append(bad_pos)

        results = []
        used = [False] * n
        current_perm = [None] * n

        def solve_dfs(depth):
            if depth == n:
                results.append("".join(current_perm))
                return

            # 遍歷每個人，看看能不能放進目前位置 (depth + 1)
            for i in range(n):
                if not used[i]:
                    person_char = chr(65 + i)
                    # 檢查此人 (person_char) 是否不想待在這個位置 (depth + 1)
                    if (depth + 1) not in disallowed[i]:
                        used[i] = True
                        current_perm[depth] = person_char
                        solve_dfs(depth + 1)
                        used[i] = False

        solve_dfs(0)

        # 輸出部分：只印出變動的部分
        last_str = ""
        for s in sorted(results):
            if not last_str:
                print(s)
            else:
                # 比較相同前綴
                diff_at = 0
                for i in range(len(s)):
                    if s[i] == last_str[i]:
                        diff_at += 1
                    else:
                        break
                print(" " * diff_at + s[diff_at:])
            last_str = s

if __name__ == "__main__":
    main()
