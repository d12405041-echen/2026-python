import sys

def solve():
    for line in sys.stdin:
        n_str = line.strip()
        if n_str == "0": break

        n = int(n_str)
        binary_str = bin(n)[2:] # remove '0b'
        p = binary_str.count('1')
        print(f"The parity of {binary_str} is {p} (mod 2).")

if __name__ == "__main__":
    solve()
