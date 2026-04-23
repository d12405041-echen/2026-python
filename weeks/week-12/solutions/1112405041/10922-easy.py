import sys

# 9 的倍數深度 (2 the 9s) - 大一小萌新版
# 題目邏輯：
# 1. 算出各位數總和，如果還不是一位數，就繼續加。
# 2. 如果最後變成 9，就是 9 的倍數。
# 3. 加了幾次才變成 9，那個次數就是「深度」。

def get_digits_sum(number_string):
    # 計算字串中每個數字加起來的總和
    total = 0
    for digit in number_string:
        total += int(digit)
    return total

def main():
    # 讀取輸入
    for line in sys.stdin:
        # 去掉換行符號
        num_str = line.strip()

        # 如果輸入是 0，就結束
        if num_str == "0":
            break

        # 先檢查能不能被 9 整除
        # 一個技巧：如果各位數總和是 9 的倍數，那原數就是 9 的倍數
        first_sum = get_digits_sum(num_str)

        if first_sum % 9 != 0:
            # 不是 9 的倍數
            print(num_str + " is not a multiple of 9.")
        else:
            # 是 9 的倍數，開始算深度
            degree = 1
            current_sum_str = str(first_sum)

            # 只要還沒變成單一位數 9，就一直加下去
            while current_sum_str != "9":
                next_sum = get_digits_sum(current_sum_str)
                current_sum_str = str(next_sum)
                degree += 1

            print(num_str + " is a multiple of 9 and has 9-degree " + str(degree) + ".")

if __name__ == "__main__":
    main()
