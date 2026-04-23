import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    n = int(input_data[0])
    idx = 1
    for _ in range(n):
        s = int(input_data[idx])
        d = int(input_data[idx+1])
        idx += 2

        # x + y = s, x - y = d => 2x = s + d, 2y = s - d
        if (s + d) % 2 != 0 or s < d:
            print("impossible")
        else:
            x = (s + d) // 2
            y = (s - d) // 2
            print(f"{x} {y}")

if __name__ == "__main__":
    solve()
