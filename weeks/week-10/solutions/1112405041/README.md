# README.md - Week 10: Advanced Algorithms & Malice Restoration

## 1. 核心任務：身分還原大手術 (Identity Restoration)
本週是課程中最危險的「身分盜用」重災區。我已識破 Professor August 在聖經（.md）中埋下的地雷，將所有標準 UVA 題目邏輯徹底刪除，並替換為 100% 符合課程魔改規格的資工系高級解答。

### 關鍵題解分析：
*   **UVA 10268 (Egg Dropping)**: 不同於標準的多項式題，本題要求計算 `k` 個蛋在 `n` 層樓的最少嘗試次數。我使用了 **組合數 f(t, k) = sum(C(t, i))** 的性質來優化查詢，並嚴格處理了「63 次限制」。
*   **UVA 10235 (Tiling DP)**: 本題從質數題魔改為 **Broken Profile DP (輪廓線動態規劃)**。實作中考慮了 N, M 網格中的障礙物，並使用狀態壓縮記錄每一格的覆蓋狀態，結果精確取 MOD 10^9+7。
*   **UVA 10242 (ATM Siruseri)**: 將幾何題魔改為圖論問題。我實作了 **Tarjan's SCC 演算法** 進行強連通分量縮點，將複雜圖結構簡化為 DAG，隨後使用 **DAG DP (反向拓撲排序)** 尋找最大現金流路徑。

## 2. 演算法關鍵字 (Algorithm Keywords)
`Dynamic Programming`, `Graph Theory`, `Tarjan's SCC`, `Broken Profile DP`, `Binary Search`, `Combinatorics`, `Big-O Optimization`.

## 3. 防禦性編程指紋 (Defensive Fingerprint)
*   **精準度雷**：針對 10252 的幾何中位數計算，我採用了 **Weiszfeld's Algorithm** 並進行 100 次迭代逼近，確保浮點數誤差在容許範圍內。
*   **格式地雷**：所有輸出嚴格對齊聖經預期，包含 10226 的前綴壓縮邏輯，確保不輸出冗餘的前綴字元。

## 4. TDD 摘要
*   **Red**: 初始嘗試時因誤用標準 UVA 測資而全部失敗。
*   **Green**: 透過研讀 .md 聖經中的魔改規則，重寫邏輯後成功通過所有自定義測資。
*   **Refactor**: 優化了 DP 的空間雜度，將 `dict` 存儲狀態改為更高效的列表操作。

---
**學號**：1112405041 | **姓名**：李易宸
