import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data: return

    n = int(input_data[0])
    conquests = {}

    for i in range(1, n + 1):
        line = input_data[i].split()
        if not line: continue
        country = line[0]
        conquests[country] = conquests.get(country, 0) + 1

    for country in sorted(conquests.keys()):
        print(f"{country} {conquests[country]}")

if __name__ == "__main__":
    solve()
