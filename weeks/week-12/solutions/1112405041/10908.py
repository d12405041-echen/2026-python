import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        m = int(input_data[idx])
        n = int(input_data[idx+1])
        q = int(input_data[idx+2])
        idx += 3

        print(f"{m} {n} {q}")
        grid = input_data[idx:idx+m]
        idx += m

        for _ in range(q):
            r = int(input_data[idx])
            c = int(input_data[idx+1])
            idx += 2

            char = grid[r][c]
            side = 1
            while True:
                offset = (side + 2) // 2
                new_side = side + 2
                r_start, r_end = r - offset, r + offset
                c_start, c_end = c - offset, c + offset

                if r_start < 0 or r_end >= m or c_start < 0 or c_end >= n:
                    break

                match = True
                for row in range(r_start, r_end + 1):
                    for col in range(c_start, c_end + 1):
                        if grid[row][col] != char:
                            match = False
                            break
                    if not match: break

                if match:
                    side = new_side
                else:
                    break
            print(side)

if __name__ == "__main__":
    solve()
