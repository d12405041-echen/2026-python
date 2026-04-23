import sys

# 公共子序列 (Common Permutation) - 大一小萌新版
# 題目邏輯：
# 給你兩行字串，找出它們「共同擁有」的字元。
# 如果 'a' 在第一個字串出現 3 次，在第二個出現 2 次，那共同擁有的就是 2 個 'a'。
# 最後要把這些字元按照字母順序排好印出來。

def main():
    # 讀取輸入，一行一行處理
    lines = sys.stdin.read().splitlines()

    i = 0
    while i < len(lines):
        s1 = lines[i]
        # 確保有第二行可以讀，不然給空字串
        if i + 1 < len(lines):
            s2 = lines[i+1]
        else:
            s2 = ""
        i += 2

        # 1. 統計第一個字串每個字母出現的次數
        count1 = {}
        for char in s1:
            if char >= 'a' and char <= 'z':
                if char in count1:
                    count1[char] += 1
                else:
                    count1[char] = 1

        # 2. 統計第二個字串每個字母出現的次數
        count2 = {}
        for char in s2:
            if char >= 'a' and char <= 'z':
                if char in count2:
                    count2[char] += 1
                else:
                    count2[char] = 1

        # 3. 找出共同的字母及其最小出現次數
        result_chars = []
        # 跑遍 a 到 z
        for code in range(ord('a'), ord('z') + 1):
            char = chr(code)
            if char in count1 and char in count2:
                # 取兩者中出現次數較少的那個
                m1 = count1[char]
                m2 = count2[char]
                common_count = m1
                if m2 < m1:
                    common_count = m2

                # 把這個字母重複加入結果清單中
                for _ in range(common_count):
                    result_chars.append(char)

        # 4. 印出結果 (因為我們是按 a-z 順序找的，所以已經排好了)
        output = ""
        for c in result_chars:
            output += c
        print(output)

if __name__ == "__main__":
    main()
