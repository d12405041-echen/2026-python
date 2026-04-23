import unittest
from template_lib import build_huffman_tree, Trie

class TestDataEncodingTemplates(unittest.TestCase):
    """
    Week 09 練習紀錄：驗證樹狀資料結構模板
    """
    def test_huffman_basic(self):
        text = "aaabbc"
        codes = build_huffman_tree(text)
        # 'a' 出現頻率最高，編碼長度應該最短
        self.assertTrue(len(codes['a']) <= len(codes['b']))
        self.assertTrue(len(codes['a']) <= len(codes['c']))
        print(f"\nHuffman Codes for '{text}': {codes}")

    def test_trie_basic(self):
        trie = Trie()
        trie.insert("apple")
        trie.insert("app")
        # 驗證結構是否正確建立 (用於 W10 排列組合的前綴過濾)
        self.assertTrue('a' in trie.root.children)
        self.assertTrue('p' in trie.root.children['a'].children)

if __name__ == '__main__':
    unittest.main()
