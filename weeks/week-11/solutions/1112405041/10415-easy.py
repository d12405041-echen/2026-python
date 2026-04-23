import sys

# 薩克斯風指法計數 (Eb Alto Saxophone Player) - 大一小萌新版
# 我們要算每一根手指頭總共「按下去」了幾次。
# 關鍵：如果本來就按著，下一個音也要按，那就不算新的次數。

def main():
    # 建立一個指法表
    # 1 代表左手大拇指, 2-4 代表左手食指、中指、無名指
    # 5-10 則是其他的按鍵
    fingers_map = {
        'c': [2, 3, 4, 7, 8, 9, 10],
        'd': [2, 3, 4, 7, 8, 9],
        'e': [2, 3, 4, 7, 8],
        'f': [2, 3, 4, 7],
        'g': [2, 3, 4],
        'a': [2, 3],
        'b': [2],
        'C': [3],
        'D': [1, 2, 3, 4, 7, 8, 9],
        'E': [1, 2, 3, 4, 7, 8],
        'F': [1, 2, 3, 4, 7],
        'G': [1, 2, 3, 4],
        'A': [1, 2, 3],
        'B': [1, 2]
    }

    # 讀取輸入
    input_text = sys.stdin.read().splitlines()
    if not input_text:
        return

    # 第一行是測試資料的組數
    num_test_cases = int(input_text[0])

    for i in range(1, num_test_cases + 1):
        # 取得這一組的旋律（音符字串）
        melody = ""
        if i < len(input_text):
            melody = input_text[i]

        # 準備 10 根手指頭的計數器
        press_counts = [0] * 11 # 索引 1 到 10
        # 記錄目前每一根手指頭的狀態 (False 表示放開，True 表示按下)
        is_currently_pressed = [False] * 11

        # 逐一處理旋律中的音符
        for note in melody:
            # 取得這個音符需要按下的手指編號清單
            needed_fingers = fingers_map[note]

            # 建立這一刻所有手指應該有的狀態
            should_be_pressed = [False] * 11
            for finger_num in needed_fingers:
                should_be_pressed[finger_num] = True

            # 檢查每一根手指：
            # 如果現在「要按」而且剛才「沒按」，計數器就加一
            for f in range(1, 11):
                if should_be_pressed[f] == True and is_currently_pressed[f] == False:
                    press_counts[f] += 1

            # 更新手指狀態，準備處理下一個音符
            for f in range(1, 11):
                is_currently_pressed[f] = should_be_pressed[f]

        # 輸出結果，從第 1 根印到第 10 根，中間用空白隔開
        result_str = ""
        for f in range(1, 11):
            result_str += str(press_counts[f])
            if f < 10:
                result_str += " "
        print(result_str)

if __name__ == "__main__":
    main()
