import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    t = int(input_data[0])
    idx = 1
    for case in range(1, t + 1):
        # Input format: N = size
        # We need to skip 'N', '=', and get the size
        idx += 2 # Skip "N" and "="
        n = int(input_data[idx])
        idx += 1

        matrix = []
        is_symmetric = True
        for _ in range(n * n):
            val = int(input_data[idx])
            idx += 1
            if val < 0: is_symmetric = False
            matrix.append(val)

        if is_symmetric:
            # Check mirror elements
            for i in range((n * n) // 2 + 1):
                if matrix[i] != matrix[n * n - 1 - i]:
                    is_symmetric = False
                    break

        if is_symmetric:
            print(f"Test #{case}: Symmetric.")
        else:
            print(f"Test #{case}: Non-symmetric.")

if __name__ == "__main__":
    solve()
