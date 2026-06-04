"""UVA 11417 — GCD 實作
"""

import math


def sum_of_gcd(n: int) -> int:
    """計算 Σ Σ gcd(i, j) for 1 ≤ i < j ≤ n"""
    g = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            g += math.gcd(i, j)
    return g
