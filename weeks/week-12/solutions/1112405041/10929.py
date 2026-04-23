import sys

def solve():
    for line in sys.stdin:
        n_str = line.strip()
        if n_str == "0": break

        # Method: sum of odd positions - sum of even positions
        odd_sum = 0
        even_sum = 0
        for i in range(len(n_str)):
            if i % 2 == 0:
                odd_sum += int(n_str[i])
            else:
                even_sum += int(n_str[i])

        if abs(odd_sum - even_sum) % 11 == 0:
            print(f"{n_str} is a multiple of 11.")
        else:
            print(f"{n_str} is not a multiple of 11.")

if __name__ == "__main__":
    solve()
