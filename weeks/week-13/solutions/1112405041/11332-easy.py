import sys

# 數位和 (Summing Digits) - 大一小萌新版
# 題目邏輯：
# 給你一個正整數 n，把它的各位數相加，得到一個新的數。
# 如果這個新的數還是兩位數以上，就重複這個過程，直到變成一位數。
# 例如：47 -> 4+7=11 -> 1+1=2

def main():
    # 讀取輸入
    for line in sys.stdin:
        # 去掉換行
        num_str = line.strip()

        # 如果輸入是 "0"，就結束
        if num_str == "0":
            break

        # 只要字串長度大於 1，就繼續加
        while len(num_str) > 1:
            total = 0
            for digit in num_str:
                total += int(digit)
            # 把加完的結果轉回字串，準備下一次迴圈判斷
            num_str = str(total)

        # 最後印出剩下的一位數
        print(num_str)

if __name__ == "__main__":
    main()
