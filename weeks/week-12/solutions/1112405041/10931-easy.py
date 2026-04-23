import sys

# 奇偶性 (Parity) - 大一小萌新版
# 題目邏輯：
# 1. 給你一個十進位整數 I。
# 2. 把它換成二進位 (例如 10 換成 1010)。
# 3. 數數看二進位裡面有幾個 "1"。

def main():
    # 讀取輸入
    for line in sys.stdin:
        # 去掉空白與換行
        s = line.strip()
        if not s:
            continue

        # 轉換成整數
        num = int(s)

        # 如果輸入是 0，代表結束
        if num == 0:
            break

        # 1. 將十進位轉成二進位字串
        # Python 內建 bin() 函式，例如 bin(10) 會得到 '0b1010'
        # 我們要把前面的 '0b' 拿掉
        binary_string = bin(num)[2:]

        # 2. 數數看字串裡面有幾個 '1'
        one_count = 0
        for char in binary_string:
            if char == '1':
                one_count += 1

        # 3. 按照格式輸出
        # The parity of B is P (mod 2).
        print("The parity of " + binary_string + " is " + str(one_count) + " (mod 2).")

if __name__ == "__main__":
    main()
