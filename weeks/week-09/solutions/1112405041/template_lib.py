import heapq
from collections import Counter

# 【August 的惡意：Week 09 隱藏任務】
# 雖然本週沒有 QUESTION-*.md，但 README 要求提交「資料結構模板與練習紀錄」。
# 提交空目錄會觸發「⚠️ 0py」處刑。
# 此檔案包含「資料編碼：樹狀與頻率」的核心模板，為後續 Week 10 的 DFS 與 10226 題作準備。

class HuffmanNode:
    """哈夫曼編碼節點：用於頻率解析與資料壓縮"""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # 為了讓 heapq 能夠比較節點 (Big-O: O(log N))
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    """建立哈夫曼樹並回傳編碼表"""
    if not text: return {}

    # 1. 統計頻率 (對應 Week 02 的 Counter)
    counter = Counter(text)

    # 2. 建立優先權隊列 (對應 Week 02 的 R5)
    pq = [HuffmanNode(char, freq) for char, freq in counter.items()]
    heapq.heapify(pq)

    # 3. 貪婪演算法合併節點
    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(pq, merged)

    # 4. 生成路徑編碼
    codes = {}
    def generate_codes(node, current_code):
        if not node: return
        if node.char is not None:
            codes[node.char] = current_code
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(pq[0], "")
    return codes

class TrieNode:
    """字典樹節點：用於前綴壓縮與字串檢索"""
    # 這是為了應付 Week 10 (10226) 的前綴壓縮輸出而準備的指紋模板
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node.current = node.children[char]
            node = node.current
        node.is_end = True

# August 學習筆記：
# 透過實作這些模板，我深刻理解了「資料編碼」不只是壓縮，
# 更多是關於如何利用「樹狀結構」來優化檢索 (Trie) 與解析 (Huffman)。
# 這是我對抗 August Hell 的預置武裝。
