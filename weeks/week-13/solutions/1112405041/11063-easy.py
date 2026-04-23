import sys

# B2 數列 (B2-Sequence) - 大一小萌新版
# 題目邏輯：
# 1. 數列必須是遞增的，且所有數字都要大於等於 1。
# 2. 任意兩個數字相加的和，不能重複出現。
# 如果符合這兩個條件，就是 B2-Sequence。

def main():
    # 讀取輸入
    input_text = sys.stdin.read().split()
    if not input_text:
        return

    idx = 0
    case_count = 1

    while idx < len(input_text):
        # N 是數列的長度
        n = int(input_text[idx])
        idx += 1

        # 讀取數列內容
        sequence = []
        is_b2 = True

        for i in range(n):
            num = int(input_text[idx])
            idx += 1

            # 條件檢查：數字要大於等於 1
            if num < 1:
                is_b2 = False
            # 條件檢查：數列必須遞增 (比前一個大)
            if i > 0 and num <= sequence[i-1]:
                is_b2 = False

            sequence.append(num)

        # 如果前面基本的遞增條件就沒過，就不用算總和了
        if is_b2 == True:
            # 用一個清單紀錄出現過的總和
            sums_found = []

            for i in range(n):
                for j in range(i, n):
                    # 計算任意兩數之和
                    total = sequence[i] + sequence[j]

                    # 檢查這個總和是不是出現過
                    already_exists = False
                    for s in sums_found:
                        if s == total:
                            already_exists = True
                            break

                    if already_exists == True:
                        is_b2 = False
                        break
                    else:
                        sums_found.append(total)

                if is_b2 == False:
                    break

        # 依照題目要求格式輸出 (注意結尾要有兩個換行符號)
        if is_b2 == True:
            print("Case #" + str(case_count) + ": It is a B2-Sequence.\n")
        else:
            print("Case #" + str(case_count) + ": It is not a B2-Sequence.\n")

        case_count += 1

if __name__ == "__main__":
    main()
