import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    ptr = 0
    while ptr < len(input_data):
        n = int(input_data[ptr])
        ptr += 1
        if n == 0: break

        # 骰子初始狀態：頂1, 北2, 西3
        # 推導：底6, 南5, 東4
        top, north, west = 1, 2, 3

        for _ in range(n):
            cmd = input_data[ptr]
            ptr += 1
            if cmd == "north":
                # 滾向北：新頂為南(5), 新北為頂(1)
                top, north = 7 - north, top
            elif cmd == "south":
                # 滾向南：新頂為北(2), 新南為頂(1) -> 新北為 7-頂
                top, north = north, 7 - top
            elif cmd == "west":
                # 滾向西：新頂為東(4), 新西為頂(1)
                top, west = 7 - west, top
            elif cmd == "east":
                # 滾向東：新頂為西(3), 新東為頂(1) -> 新西為 7-頂
                top, west = west, 7 - top

        sys.stdout.write(str(top) + "\n")

if __name__ == "__main__":
    solve()
