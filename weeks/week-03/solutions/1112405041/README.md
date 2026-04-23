# Week 03 程式碼執行說明

本週作業包含五題 UVA 題目與 Robot Lost 遊戲實作，所有解答皆放置於 `weeks/week-03/solutions/1112405041/` 目錄下。

## 完成題號
- QUESTION-100 (UVA 100 - The 3n+1 Problem)
- QUESTION-118 (UVA 118 - Martian Robots)
- QUESTION-272 (UVA 272 - TEX Quotes)
- QUESTION-299 (UVA 299 - Train Swapping)
- QUESTION-490 (UVA 490 - Rotating Sentences)
- Robot Lost Game (pygame MVP)

## 執行方式
您可以執行測試腳本來驗證正確性（推薦）：
```bash
# 執行所有測試
python -m unittest discover .

# 啟動機器人遊戲 (需安裝 pygame)
python robot_game.py
```

## 依賴套件
- Python 3.10+
- `pygame` (用於執行 robot_game.py)
- `unittest` (內建套件)

## 遊戲開發證據紀錄
- **偵破點**：我發現 `HOMEWORK.md` 要求實作的 `robot_game.py` 其實是為了後續遊戲引擎的座標與碰撞偵測做鋪路。
- **偵破點**：`scent` 邏輯的實作是為了處理遊戲中的「障礙物記憶」機制。
