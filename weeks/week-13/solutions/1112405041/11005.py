import sys

def solve():
    # 使用更加強健的輸入讀取
    input_data = sys.stdin.read().split()
    if not input_data: return

    try:
        t = int(input_data[0])
    except: return

    idx = 1
    for case in range(1, t + 1):
        if idx + 36 > len(input_data): break
        costs = list(map(int, input_data[idx:idx+36]))
        idx += 36

        if idx >= len(input_data): break
        q = int(input_data[idx])
        idx += 1

        if case > 1: sys.stdout.write("\n")
        sys.stdout.write(f"Case {case}:\n")

        for _ in range(q):
            if idx >= len(input_data): break
            num = int(input_data[idx])
            idx += 1

            min_cost = float('inf')
            best_bases = []

            for base in range(2, 37):
                current_cost = 0
                temp_num = num
                if temp_num == 0:
                    current_cost = costs[0]
                else:
                    while temp_num > 0:
                        current_cost += costs[temp_num % base]
                        temp_num //= base

                if current_cost < min_cost:
                    min_cost = current_cost
                    best_bases = [base]
                elif current_cost == min_cost:
                    best_bases.append(base)

            sys.stdout.write(f"Cheapest base(s) for number {num}: {' '.join(map(str, best_bases))}\n")

if __name__ == "__main__":
    solve()
