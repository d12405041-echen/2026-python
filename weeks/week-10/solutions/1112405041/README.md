# Week 10 程式碼執行說明

本週作業包含五題 UVA 題目，主要訓練排序、質數判定、幾何運算、字串頻率統計以及多項式求導。

## 檔案結構
- `[題號].py`: 標準版解法。
- `[題號]-easy.py`: 基礎語法版（含詳細繁體中文註解）。
- `test_[題號].py`: 單元測試檔。

## 執行方式
```bash
# 執行反轉質數題目
python 10235.py < input.txt

# 執行測試驗證
python -m unittest test_10226.py
python -m unittest test_10235.py
python -m unittest test_10242.py
python -m unittest test_10252.py
python -m unittest test_10268.py
```

## 題目清單
1. UVA 10226 - Permutations (依 MD 敘述)
2. UVA 10235 - Simply Emirp
3. UVA 10242 - Fourth Point
4. UVA 10252 - Common Permutation
5. UVA 10268 - 498-bis (多項式導數)
