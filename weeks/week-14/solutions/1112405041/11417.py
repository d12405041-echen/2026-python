import sys
import math

def solve():
    for line in sys.stdin:
        n_str = line.strip()
        if not n_str or n_str == "0": break
        n = int(n_str)

        g = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                g += math.gcd(i, j)
        print(g)

if __name__ == "__main__":
    solve()
