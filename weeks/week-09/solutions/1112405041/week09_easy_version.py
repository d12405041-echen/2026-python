# AI 教導的簡單版本：字典樹與頻率統計
# 此版本專注於理解樹狀結構的遞迴邏輯

class SimpleNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class SimpleTrie:
    def __init__(self):
        self.root = SimpleNode()

    def insert(self, word):
        """插入一個單字"""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = SimpleNode()
            current = current.children[char]
        current.is_word = True

    def search(self, word):
        """搜尋一個單字是否存在"""
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_word

# 簡單版本示範了基礎的字典樹結構
# 幫助理解如何透過嵌套字典 (Dict) 實作樹狀分層
