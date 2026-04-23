import sys

# 對稱矩陣 (Symmetric Matrix) - 大一小萌新版
# 題目邏輯：
# 1. 矩陣裡面的數字不能有負數。
# 2. 矩陣必須「對稱」，也就是說，把矩陣拉成一條長龍，頭尾對應的數字要一模一樣。

def main():
    # 讀取輸入
    input_text = sys.stdin.read().split()
    if not input_text:
        return

    # 測試組數
    num_cases = int(input_text[0])
    idx = 1

    for case_idx in range(1, num_cases + 1):
        # 題目格式是 "N = 3"，我們要把 "N" 和 "=" 略過
        idx += 2
        # 讀取矩陣大小
        n = int(input_text[idx])
        idx += 1

        # 讀取整個矩陣的所有數字
        matrix_data = []
        is_still_symmetric = True

        for i in range(n * n):
            val = int(input_text[idx])
            idx += 1
            # 規則 1：如果有負數，就一定不對稱
            if val < 0:
                is_still_symmetric = False
            matrix_data.append(val)

        # 規則 2：檢查頭尾對應
        if is_still_symmetric == True:
            total_elements = n * n
            # 我們只要檢查前一半就可以了
            for i in range(total_elements // 2 + 1):
                # 頭對尾、二對倒數二...
                if matrix_data[i] != matrix_data[total_elements - 1 - i]:
                    is_still_symmetric = False
                    break

        # 輸出結果
        if is_still_symmetric == True:
            print("Test #" + str(case_idx) + ": Symmetric.")
        else:
            print("Test #" + str(case_idx) + ": Non-symmetric.")

if __name__ == "__main__":
    main()
