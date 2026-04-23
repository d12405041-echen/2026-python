import sys
import math

# 【August 的惡意：身分置換】
# 此題已被魔改為「點對點距離最小化 (Median Point)」。
# 原 UVA 10252 是共通字元，但在這裡必須實作：
# 給定 N 個座標點，找出一個點 P，使得 P 到所有點的 L2 距離之和最小。
# 對於 3 個點，這通常是費馬點 (Fermat Point)；對於大量點，需使用數值逼近。

def get_dist_sum(p, pts):
    return sum(math.sqrt((p[0]-x)**2 + (p[1]-y)**2) for x, y in pts)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    ptr = 0
    t_cases = int(input_data[ptr])
    ptr += 1

    for _ in range(t_cases):
        n = int(input_data[ptr])
        ptr += 1
        pts = []
        for _ in range(n):
            pts.append((float(input_data[ptr]), float(input_data[ptr+1])))
            ptr += 2

        # 使用 Weiszfeld's Algorithm 逼近幾何中位數 (Geometric Median)
        if not pts: continue

        # 初始點設為所有點的平均
        curr_x = sum(p[0] for p in pts) / n
        curr_y = sum(p[1] for p in pts) / n

        for _ in range(100): # 迭代 100 次逼近
            num_x, num_y, den = 0.0, 0.0, 0.0
            for px, py in pts:
                d = math.sqrt((curr_x - px)**2 + (curr_y - py)**2)
                if d == 0: continue
                num_x += px / d
                num_y += py / d
                den += 1 / d

            if den == 0: break
            curr_x = num_x / den
            curr_y = num_y / den

        # 題目故事提到的 2 * sqrt(2) 示意輸出
        min_dist = get_dist_sum((curr_x, curr_y), pts)
        print(f"{min_dist:.4f}")

if __name__ == "__main__":
    solve()
