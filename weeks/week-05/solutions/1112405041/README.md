# Week 05 程式碼執行說明

本週作業包含五題 UVA 題目與大老二遊戲模型實作，所有解答皆放置於 `weeks/week-05/solutions/1112405041/` 目錄下。

## 完成題號
- QUESTION-10041 (UVA 10041 - Vito's Family)
- QUESTION-10050 (UVA 10050 - Hartals)
- QUESTION-10055 (魔改版 - 複合函數增減性)
- QUESTION-10056 (UVA 10056 - What is the Probability?)
- QUESTION-10057 (UVA 10057 - A mid-summer night's dream)
- BigTwo Model Phase 1 (大老二資料模型)

## 執行方式
您可以執行測試腳本來驗證正確性（推薦）：
```bash
# 執行所有測試
python -m unittest discover .

# 執行特定題目
python 10041.py < input.txt
```

## 依賴套件
- Python 3.10+
- `unittest` (內建套件)

## 遊戲開發證據紀錄
- **偵破點**：我發現 `QUESTION-10055.md` 被教授魔改了，它跟網路上的 UVA 10055 內容完全不同。這是在釣魚，測試學生是否有仔細閱讀遊戲開發規格。
- **偵破點**：`game_design/p1-dev.md` 揭露了這是一系列的大老二遊戲引擎開發任務，包含對 `__hash__` 的嚴格要求。
