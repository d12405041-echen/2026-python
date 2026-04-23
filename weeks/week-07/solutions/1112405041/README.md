# Week 07 程式碼執行說明

本週作業包含五題 UVA 題目與赤壁戰役遊戲引擎實作，所有解答皆放置於 `weeks/week-07/solutions/1112405041/` 目錄下。

## 完成題號
- QUESTION-10062 (UVA 10062 - Tell me the frequencies!)
- QUESTION-10071 (魔改版 - 六元組總和)
- QUESTION-10093 (UVA 10093 - 炮兵布陣)
- QUESTION-10101 (魔改版 - 移動火柴棒)
- QUESTION-10170 (UVA 10170 - The Hotel with Infinite Rooms)
- Chibi Battle Engine (赤壁戰役戰鬥引擎)

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
- **偵破點**：我發現 `QUESTION-10071` 和 `QUESTION-10101` 內容完全與 UVA 官方題目不同，這是教授故意測試學生是否有仔細閱讀遊戲開發聖經 (.md) 的陷阱。
- **偵破點**：`chibi_battle.py` 整合了前幾週的所有資料結構，是遊戲核心邏輯模組。
