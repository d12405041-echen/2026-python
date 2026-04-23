import sys

def get_sum(s):
    return sum(int(digit) for digit in s)

def solve():
    for line in sys.stdin:
        n_str = line.strip()
        if n_str == "0": break

        if int(n_str) % 9 != 0:
            print(f"{n_str} is not a multiple of 9.")
        else:
            degree = 1
            curr_sum = str(get_sum(n_str))
            while curr_sum != "9":
                curr_sum = str(get_sum(curr_sum))
                degree += 1
            print(f"{n_str} is a multiple of 9 and has 9-degree {degree}.")

if __name__ == "__main__":
    solve()
