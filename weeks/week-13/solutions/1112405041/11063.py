import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    case_num = 1
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        b = []
        is_b2 = True
        for i in range(n):
            val = int(input_data[idx])
            idx += 1
            if val < 1: is_b2 = False
            if b and val <= b[-1]: is_b2 = False
            b.append(val)

        if is_b2:
            sums = set()
            for i in range(n):
                for j in range(i, n):
                    s = b[i] + b[j]
                    if s in sums:
                        is_b2 = False
                        break
                    sums.add(s)
                if not is_b2: break

        if is_b2:
            print(f"Case #{case_num}: It is a B2-Sequence.\n")
        else:
            print(f"Case #{case_num}: It is not a B2-Sequence.\n")
        case_num += 1

if __name__ == "__main__":
    solve()
