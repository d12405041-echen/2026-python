import sys

# 11 的倍數判定 - 大一小萌新版
# 題目邏輯：
# 給你一個很大的數字（字串形式），判斷它是不是 11 的倍數。
# 技巧：(奇數位數之和) 減 (偶數位數之和) 的結果，如果能被 11 整除，那原數就是 11 的倍數。

def main():
    # 讀取輸入
    for line in sys.stdin:
        # 去掉頭尾空白和換行
        num_str = line.strip()

        # 如果輸入是 "0"，就結束
        if num_str == "0":
            break

        # 初始化奇數位與偶數位的總和
        odd_sum = 0
        even_sum = 0

        # 逐一檢查字串中的每個位數
        # 索引 i 從 0 開始 (0 是偶數，對應第 1 位，即奇數位置)
        for i in range(len(num_str)):
            digit = int(num_str[i])

            if i % 2 == 0:
                # 索引 0, 2, 4... (第 1, 3, 5... 位)
                odd_sum += digit
            else:
                # 索引 1, 3, 5... (第 2, 4, 6... 位)
                even_sum += digit

        # 計算兩者的差 (取絕對值)
        diff = odd_sum - even_sum
        if diff < 0:
            diff = -diff

        # 如果差值可以被 11 整除，那就是 11 的倍數
        if diff % 11 == 0:
            print(num_str + " is a multiple of 11.")
        else:
            print(num_str + " is not a multiple of 11.")

if __name__ == "__main__":
    main()
