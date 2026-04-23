import sys

def get_pos(x, y):
    # Sum of all nodes in rows above current diagonal:
    # Row 0: (0,0) -> 1 node
    # Row 1: (0,1),(1,0) -> 2 nodes
    # Row 2: (0,2),(1,1),(2,0) -> 3 nodes
    # For point (x,y), let s = x+y
    # Nodes in rows 0 to s-1: (s*(s+1)) // 2
    # Current node in diagonal s: x + 1 (starting from (0,s) as 1st node)
    s = x + y
    return (s * (s + 1)) // 2 + x

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    n = int(input_data[0])
    idx = 1
    for i in range(1, n + 1):
        x1 = int(input_data[idx])
        y1 = int(input_data[idx+1])
        x2 = int(input_data[idx+2])
        y2 = int(input_data[idx+3])
        idx += 4

        steps = get_pos(x2, y2) - get_pos(x1, y1)
        print(f"Case {i}: {steps}")

if __name__ == "__main__":
    solve()
