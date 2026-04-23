# Week 09 深度複習：資料編碼、結構化解析與頻率統計

本週是全學期最重要的「邏輯沉澱週」。我們不再追逐題目的數量，而是專注於「資料編碼」的本質。透過整理結構化解析與頻率統計模板，我對如何將雜亂的輸入轉換為高效的資料結構有了全新的理解。

## 🛠️ 1. 結構化解析模板 (Structured Parsing)
針對複雜的、非規律的字串，我們需要一套萬用的解析邏輯。

```python
import sys

def structured_parser():
    """將每一行輸入解析為字典格式，方便後續查詢"""
    # 範例資料: "ID:10226 | Type:Tree | Value:99"
    parsed_data = []
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        
        # 使用多重分割或字典推導式
        record = {}
        parts = line.split('|')
        for part in parts:
            key, value = part.split(':')
            record[key.strip()] = value.strip()
        parsed_data.append(record)
    return parsed_data
```

---

## 🌲 2. 頻率統計與樹狀節點 (Tree & Frequency)
針對 CPE 常考的字元統計（如 10008, 10252），字典結合 Lambda 排序是最高效的寫法。

### 🔹 高階頻率統計模板
```python
from collections import Counter

def frequency_analyzer(text):
    # 只統計英文字母並轉小寫
    clean_text = [char.lower() for char in text if char.isalpha()]
    
    # 使用 Counter 進行極速統計
    counts = Counter(clean_text)
    
    # 按照「出現次數降序」且「字母升序」排列 (CPE 經典要求)
    sorted_res = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    for char, count in sorted_res:
        print(f"{char.upper()} {count}")
```

### 🔹 樹狀結構節點 (為 Huffman 編碼鋪路)
理解頻率後，下一個階段就是將頻率轉換為樹狀編碼。

```python
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    # 為了能放入優先佇列，定義比較邏輯
    def __lt__(self, other):
        return self.freq < other.freq

# 建立簡單的二元搜尋樹節點
def insert_node(root, char, freq):
    if root is None:
        return Node(char, freq)
    if freq < root.freq:
        root.left = insert_node(root.left, char, freq)
    else:
        root.right = insert_node(root.right, char, freq)
    return root
```

---

## 💡 期末衝刺心得
整理完這些模板後，我發現原本在 Week 04 覺得很痛苦的 10008（字母頻率），現在只要用 `Counter` 加上一行 `sorted()` 就能解掉。這就是「資料結構」帶來的維度提升。

我已經預習了 Week 10 的五道題目，發現它們幾乎都逃不出「字典、排序、搜尋」這三大核心。這週的模板整理讓我對接下來的 19 題實彈轟炸充滿了信心！
