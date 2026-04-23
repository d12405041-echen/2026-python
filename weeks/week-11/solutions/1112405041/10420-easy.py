import sys

# 征服名單 (List of Conquests) - 大一小萌新版
# 題目要求：算算看唐·喬凡尼在每個國家到底征服了幾位女性。
# 給你的資料長這樣：「國家名稱 女性姓名」，我們只要統計國家出現的次數。
# 最後要按照國家的名字從小到大排序。

def main():
    # 讀取所有的輸入行
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return

    # 第一行是資料的筆數
    num_records = int(input_lines[0])

    # 我們使用一個「字典」來儲存每個國家的人數
    # 字典的格式會是 { "國家名字": 人數 }
    country_counts = {}

    for i in range(1, num_records + 1):
        # 取得每一行的內容
        line = input_lines[i]
        # 把這一行切割成一個一個的單字
        parts = line.split()

        # 如果這一行是空的，就跳過
        if len(parts) == 0:
            continue

        # 第一個單字一定是國家名稱
        country_name = parts[0]

        # 檢查這個國家是否已經在我們的統計字典裡了
        if country_name in country_counts:
            # 如果已經有了，就把人數加 1
            country_counts[country_name] = country_counts[country_name] + 1
        else:
            # 如果還沒有，就初始化這個國家的人數為 1
            country_counts[country_name] = 1

    # 為了按字母順序輸出，我們先把字典裡所有的「國家名稱」抓出來排好序
    sorted_countries = sorted(country_counts.keys())

    # 按照排好的順序，印出國家名稱和人數
    for name in sorted_countries:
        count = country_counts[name]
        print(name + " " + str(count))

if __name__ == "__main__":
    main()
