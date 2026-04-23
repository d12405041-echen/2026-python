import unittest
import os
from week09_template_lib import build_huffman_tree, Trie, analyze_file_frequencies

class TestDataEncodingTemplates(unittest.TestCase):
    """
    Week 09 練習紀錄：驗證樹狀與 File I/O 模板
    """
    def test_huffman_basic(self):
        text = "aaabbc"
        codes = build_huffman_tree(text)
        # 'a' 出現頻率最高，編碼長度應該最短
        self.assertTrue(len(codes['a']) <= len(codes['b']))
        self.assertTrue(len(codes['a']) <= len(codes['c']))
        print(f"\nHuffman Codes for '{text}': {codes}")

    def test_trie_advanced(self):
        trie = Trie()
        trie.insert("apple")
        trie.insert("app")
        trie.insert("application")
        # 驗證前綴計數功能 (用於數據分析)
        self.assertEqual(trie.get_count("app"), 3)
        self.assertEqual(trie.get_count("appl"), 2)
        self.assertTrue('a' in trie.root.children)

    def test_file_io_analysis(self):
        # 建立暫時測試檔 (模擬 04/23 File Task)
        test_file = "temp_test.txt"
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write("hello world")

        freqs = analyze_file_frequencies(test_file)
        self.assertEqual(freqs['l'], 3)
        self.assertEqual(freqs['h'], 1)

        if os.path.exists(test_file):
            os.remove(test_file)

if __name__ == '__main__':
    unittest.main()
