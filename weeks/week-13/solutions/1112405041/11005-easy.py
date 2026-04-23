import sys

# 最便宜進位制 (Cheapest Base) - 大一小萌新版
# 題目邏輯：
# 給你 2 到 36 進位中，每個字元所需的成本。
# 針對一組數字，算出在哪個進位制下的總成本最低。

def main():
    # 讀取輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # 測試組數
    num_cases = int(input_data[0])
    idx = 1

    for case_idx in range(1, num_cases + 1):
        # 1. 讀取 36 個數字的成本 (對應 0-9, A-Z)
        char_costs = []
        for i in range(36):
            char_costs.append(int(input_data[idx]))
            idx += 1

        # 2. 讀取查詢數量
        num_queries = int(input_data[idx])
        idx += 1

        # 格式要求：Case 之間要有空行
        if case_idx > 1:
            print()
        print("Case " + str(case_idx) + ":")

        # 3. 處理每個查詢數字
        for q in range(num_queries):
            target_num = int(input_data[idx])
            idx += 1

            # 記錄 2 到 36 進位中，最低的成本是多少
            min_cost = 999999999
            # 記錄哪些進位制達到這個最低成本
            best_bases = []

            for base in range(2, 37):
                current_total = 0
                temp = target_num

                # 如果數字是 0，特別處理
                if temp == 0:
                    current_total = char_costs[0]
                else:
                    # 進位制轉換邏輯
                    while temp > 0:
                        remainder = temp % base
                        current_total += char_costs[remainder]
                        temp = temp // base

                # 更新最低成本與對應進位制
                if current_total < min_cost:
                    min_cost = current_total
                    best_bases = [base]
                elif current_total == min_cost:
                    best_bases.append(base)

            # 輸出結果
            bases_str = ""
            for i in range(len(best_bases)):
                bases_str += str(best_bases[i])
                if i < len(best_bases) - 1:
                    bases_str += " "
            print("Cheapest base(s) for number " + str(target_num) + ": " + bases_str)

if __name__ == "__main__":
    main()
