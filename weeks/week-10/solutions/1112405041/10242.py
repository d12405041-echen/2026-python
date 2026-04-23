import sys

# 【August 的惡意：身分置換】
# 此題已被魔改為「Siruseri City ATM 圖論問題」。
# 原 UVA 10242 是平行四邊形第四點，但在這裡必須實作：
# 給定 N 個節點(ATM)與 M 條單向路徑，以及起點 S 與終點集合 P。
# 找出從 S 到達任意終點 P 所能收集到的最大現金總和。

# 核心算法：Tarjan SCC 強連通分量縮點 + DAG 動態規劃

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2

        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            adj[u].append(v)
            idx += 2

        atm_values = [0] * (n + 1)
        for i in range(1, n + 1):
            atm_values[i] = int(input_data[idx])
            idx += 1

        start_node = int(input_data[idx])
        p_count = int(input_data[idx+1])
        idx += 2

        exits = set()
        for _ in range(p_count):
            exits.add(int(input_data[idx]))
            idx += 1

        # 1. Tarjan's SCC
        dfn = [0] * (n + 1)
        low = [0] * (n + 1)
        stack = []
        in_stack = [False] * (n + 1)
        timer = 0
        scc_id = [0] * (n + 1)
        scc_count = 0

        def tarjan(u):
            nonlocal timer, scc_count
            timer += 1
            dfn[u] = low[u] = timer
            stack.append(u)
            in_stack[u] = True

            for v in adj[u]:
                if not dfn[v]:
                    tarjan(v)
                    low[u] = min(low[u], low[v])
                elif in_stack[v]:
                    low[u] = min(low[u], dfn[v])

            if low[u] == dfn[u]:
                scc_count += 1
                while True:
                    node = stack.pop()
                    in_stack[node] = False
                    scc_id[node] = scc_count
                    if node == u: break

        for i in range(1, n + 1):
            if not dfn[i]: tarjan(i)

        # 2. Condense Graph into DAG
        scc_value = [0] * (scc_count + 1)
        scc_exit = [False] * (scc_count + 1)
        scc_adj = [set() for _ in range(scc_count + 1)]

        for i in range(1, n + 1):
            sid = scc_id[i]
            scc_value[sid] += atm_values[i]
            if i in exits: scc_exit[sid] = True
            for v in adj[i]:
                if scc_id[i] != scc_id[v]:
                    scc_adj[scc_id[i]].add(scc_id[v])

        # 3. DAG DP (Reverse Topological Sort)
        dp = [-1] * (scc_count + 1)

        def get_max_cash(sid):
            if dp[sid] != -1: return dp[sid]

            res = 0
            has_valid_path = scc_exit[sid]

            for next_sid in scc_adj[sid]:
                val = get_max_cash(next_sid)
                if val > 0 or scc_exit[next_sid]:
                    res = max(res, val)
                    has_valid_path = True

            if not has_valid_path:
                dp[sid] = 0
            else:
                dp[sid] = res + scc_value[sid]
            return dp[sid]

        print(get_max_cash(scc_id[start_node]))

if __name__ == "__main__":
    solve()
