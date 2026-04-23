import sys

# 根據 QUESTION-11321.md (真正的聖經)：這不是排序題！
# 魔改為「柏油路陷阱連通性判斷」。
# 規則：在 N*M 地圖放陷阱，確保左側到右側仍連通。

def solve():
    data = sys.stdin.read().split()
    if not data: return
    n, m, t = int(data[0]), int(data[1]), int(data[2])

    grid = [[0 for _ in range(m)] for _ in range(n)]

    def can_cross():
        # BFS 檢查連通性
        q = [(i, 0) for i in range(n) if grid[i][0] == 0]
        v = set(q)
        ptr = 0
        while ptr < len(q):
            r, c = q[ptr]; ptr += 1
            if c == m - 1: return True
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0 and (nr, nc) not in v:
                    v.add((nr, nc)); q.append((nr, nc))
        return False

    idx = 3
    for _ in range(t):
        x, y = int(data[idx]), int(data[idx+1]); idx += 2
        grid[x][y] = 1
        if can_cross():
            sys.stdout.write("<(_ _)>\n")
        else:
            grid[x][y] = 0
            sys.stdout.write(">_<\n")

if __name__ == "__main__":
    solve()
