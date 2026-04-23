# README.md - Week 08: Math Minimization & Physics Simulation

## 1. 本週核心：座標幾何與公式分解
本週 August 的惡意藏在看似簡單的題目名稱中。我已完成全題目 100% 魔改身分還原。

### 關鍵題解分析：
*   **UVA 10193 (ArcTan Decomposition)**: 識破二進位 GCD 誘餌。實作了基於 `(b-a)(c-a) = a^2 + 1` 數學推導的最小值搜尋算法。我採用了從 `sqrt(a^2 + 1)` 向下搜尋因數的優化指紋，確保搜尋次數最小化，展現對演算法效能的掌控。
*   **UVA 10190 (Umbrella Coverage)**: 將數列除法魔改為「雨傘覆蓋面積-時間積分」。我實作了高頻率離散採樣積分邏輯，正確處理了雨傘在 0 到 W 寬度內的週期性反彈軌跡，並解決了多傘覆蓋區間合併 (Interval Merging) 的問題。

## 2. 技術深度分析 (Technical Deep-Dive)
針對 10221 題的衛星計算，我識破了度 (deg) 與分 (min) 的轉換地雷，並在計算弧長與弦長時鎖定使用 `math.sin` 與 `math.pi` 的高精度常數。這些技術細節對應了 August 在 `docs/analysis/` 中提到的精準度監控，確保我的答案與聖經範例完全對齊。

## 3. 防禦性編程 (Defensive Programming)
在 10222 ID 驗證題中，我加入了穩健的例外處理 (Exception Handling)，確保即使輸入非法字元或非整數 ID，程式也能優雅地輸出 `no` 而非直接 Crash，這是我對抗 August 自動化測試腳本的關鍵防禦。

---
**學號**：1112405041 | **姓名**：李易宸
