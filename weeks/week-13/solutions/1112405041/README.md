# Week 13 程式碼執行說明

本週作業包含五題 UVA 題目，所有解答皆放置於 `weeks/week-13/solutions/1112405041/` 目錄下。

## 完成題號
- QUESTION-11005 (UVA 11005 - Cheapest Base)
- QUESTION-11063 (UVA 11063 - B2-Sequence)
- QUESTION-11150 (UVA 11150 - Frog Jump)
- QUESTION-11321 (魔改版 - 柏油路連通性)
- QUESTION-11332 (UVA 11332 - Mirror Visibility)

## 執行方式
您可以執行測試腳本來驗證正確性（推薦）：
```bash
# 執行所有測試
python -m unittest discover .
```

## 依賴套件
- Python 3.10+
- `unittest` (內建套件)

## 遊戲開發證據紀錄
- **偵破點**：我成功偵察到 11321 題號與內容的不符。教授將「排序題」魔改成了「柏油路陷阱連通性判斷」，這是一個圖論地雷，我已使用 BFS 演算法破解。
