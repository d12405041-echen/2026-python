import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    idx = 0
    while idx < len(input_data):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        idx += 2
        if a == 0 and b == 0: break

        # Count squares in [a, b]
        # start = ceil(sqrt(a)), end = floor(sqrt(b))
        start = math.ceil(math.sqrt(a))
        end = math.floor(math.sqrt(b))

        if start > end:
            print(0)
        else:
            print(end - start + 1)

if __name__ == "__main__":
    solve()
