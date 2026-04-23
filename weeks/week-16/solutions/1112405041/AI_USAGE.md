# AI_USAGE.md - 程式效能分析與「記憶體鎖死」紀錄

## 🤖 AI 協作紀錄

### 1. 我問 AI 的 3 個問題
*   當 N=15 時，`itertools.permutations` 為什麼會導致系統崩潰？
*   如何在 Python 中監測一段程式碼的真實執行時間 (Precision Timer)？
*   針對大量的 IO 操作，`sys.stdout.write` 與 `print` 的底層效能差異在哪？

### 2. 我採用的建議
*   **Backtracking 剪枝**：AI 教會了我如何在 DFS 過程中進行剪枝，這讓原本跑不動的 10226 題在 0.1 秒內噴出所有結果。
*   **Time profiling**：採用了 `time.perf_counter()` 來精確測量演算法的優劣。

### 3. 我拒絕的建議
*   **拒絕增加虛擬記憶體**：AI 建議如果 Android Studio 卡頓就增加 Pagefile。我拒絕了，因為我知道核心問題在於 Flex Mode 的 RAM 通道限制，我堅持用優化代碼來解決效能問題。

### 4. AI 錯誤修正案例
*   **遞迴深度 Bug**：AI 沒發現 Python 的遞迴深度限制在處理 W13 柏油路 BFS 時可能觸發。
*   **手動修正**：我手動加入了 `sys.setrecursionlimit(2000)`，確保了深層路徑的正確性。

---
**學號**：1112405041 | **姓名**：李易宸
