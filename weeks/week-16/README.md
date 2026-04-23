# Week 16 - 效能極限戰：Android Studio 與 Python 的深度對話

## 完成題號
- 10226 性能優化 (DFS Backtracking with Pruning)
- 全週次程式強健性測試

## 執行方式
- python -m unittest discover .

## 依賴套件
- Python 3.10+

## 遊戲開發證據紀錄
- **偵破點**：我發現 `studio64.exe.vmoptions` 的配置與專案 indexing 速度高度相關。這教授不僅在考程式，還在考我們對開發工具鏈的掌控。
- **偵破點**：10226 的 N=15 限制就是為了讓我們領悟「剪枝」在遊戲引擎（如路徑搜尋）中的重要性。
