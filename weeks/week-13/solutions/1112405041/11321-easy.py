import sys

# 柏油路連通性判斷 - 大一小萌新簡單版
# 雖然題目編號是 11321，但讀完 .md 就知道這絕對不是排序題！
# 💡 破解思路：每次要放陷阱，就跑一次 BFS (廣度優先搜尋) 檢查路還通不通。

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    # n: 高度, m: 寬度, t: 陷阱總數
    n, m, t = int(input_data[0]), int(input_data[1]), int(input_data[2])

    # 建立地圖
    road = [[0 for _ in range(m)] for _ in range(n)]

    ptr = 3
    for _ in range(t):
        x, y = int(input_data[ptr]), int(input_data[ptr+1])
        ptr += 2

        # 暫時放個陷阱
        road[x][y] = 1

        # 檢查是否還有路可以通到最右邊
        queue = []
        for i in range(n):
            if road[i][0] == 0: queue.append((i, 0))

        visited = set(queue)
        found = False
        while queue:
            curr_x, curr_y = queue.pop(0)
            if curr_y == m - 1:
                found = True
                break

            # 走四個方向
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = curr_x + dx, curr_y + dy
                if 0 <= nx < n and 0 <= ny < m and road[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        if found:
            print("<(_ _)>")
        else:
            # 路被封死了，把陷阱拿掉
            road[x][y] = 0
            print(">_<")

if __name__ == "__main__":
    main()
