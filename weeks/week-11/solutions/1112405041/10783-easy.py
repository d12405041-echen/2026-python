import sys

# 字母大冒險 - 大一入門版
# 雖然題目寫 10783，但內容是要找字串中「最長且連號」的英文子字串。
# 例如：'abc' 長度是 3，'xyz' 長度也是 3。

def main():
    # 讀取一整串文字
    text = sys.stdin.read().strip()
    if not text:
        return

    # 我們只處理小寫字母
    clean_text = ""
    for char in text:
        if char >= 'a' and char <= 'z':
            clean_text += char

    if not clean_text:
        return

    # 記錄目前找到的最長長度與字串
    max_length = 0
    final_best_string = ""

    current_length = 1
    current_string = clean_text[0]

    # 從第二個字開始看
    for i in range(1, len(clean_text)):
        # 如果這個字剛好是前一個字的下一個 (例如 a 後面是 b)
        if ord(clean_text[i]) == ord(clean_text[i-1]) + 1:
            current_length += 1
            current_string += clean_text[i]
        else:
            # 斷掉了，重新算
            current_length = 1
            current_string = clean_text[i]

        # 如果目前的長度 大於或等於 (題目說要最後出現的那一個) 紀錄
        if current_length >= max_length:
            max_length = current_length
            final_best_string = current_string

    # 最後印出：長度 + 該字串
    print(f"{max_length}{final_best_string}", end="")

if __name__ == "__main__":
    main()
