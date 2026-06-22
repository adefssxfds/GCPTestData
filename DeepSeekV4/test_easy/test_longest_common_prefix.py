import unittest
from typing import List


# 假设所有实现函数已经定义（复制自题目）
def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
    return strs[0]


def longest_common_prefix_horizontal(strs: List[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def longest_common_prefix_divide_conquer(strs: List[str]) -> str:
    if not strs:
        return ""

    def lcp_helper(left: int, right: int) -> str:
        if left == right:
            return strs[left]
        mid = (left + right) // 2
        lcp_left = lcp_helper(left, mid)
        lcp_right = lcp_helper(mid + 1, right)
        return common_prefix(lcp_left, lcp_right)

    def common_prefix(s1: str, s2: str) -> str:
        min_len = min(len(s1), len(s2))
        for i in range(min_len):
            if s1[i] != s2[i]:
                return s1[:i]
        return s1[:min_len]

    return lcp_helper(0, len(strs) - 1)


def longest_common_prefix_trie(strs: List[str]) -> str:
    if not strs:
        return ""

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False

    root = TrieNode()
    for s in strs:
        node = root
        for char in s:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    prefix = []
    node = root
    while len(node.children) == 1 and not node.is_end:
        char = next(iter(node.children))
        prefix.append(char)
        node = node.children[char]
    return "".join(prefix)


class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        # 四种待测试的实现
        self.algorithms = [
            ("垂直扫描", longest_common_prefix),
            ("水平扫描", longest_common_prefix_horizontal),
            ("分治法", longest_common_prefix_divide_conquer),
            ("Trie", longest_common_prefix_trie),
        ]

    def test_examples(self):
        """题目给出的两个示例"""
        test_cases = [
            (["flower", "flow", "flight"], "fl"),
            (["dog", "racecar", "car"], ""),
        ]
        for strs, expected in test_cases:
            for name, func in self.algorithms:
                with self.subTest(strs=strs, algorithm=name):
                    self.assertEqual(func(strs), expected)

    def test_single_string(self):
        """只有一个字符串"""
        test_cases = [
            (["a"], "a"),
            (["abcde"], "abcde"),
            ([""], ""),
            (["   "], "   "),  # 空格也是字符
        ]
        for strs, expected in test_cases:
            for name, func in self.algorithms:
                with self.subTest(strs=strs, algorithm=name):
                    self.assertEqual(func(strs), expected)

    def test_all_identical(self):
        """所有字符串完全相同"""
        test_cases = [
            (["aaa", "aaa", "aaa"], "aaa"),
            (["abc", "abc"], "abc"),
            (["", "", ""], ""),
        ]
        for strs, expected in test_cases:
            for name, func in self.algorithms:
                with self.subTest(strs=strs, algorithm=name):
                    self.assertEqual(func(strs), expected)

    def test_no_common_prefix(self):
        """无公共前缀"""
        test_cases = [
            (["abc", "def", "ghi"], ""),
            (
                ["ab", "ac", "ad"],
                "",
            ),  # 第一个字符相同？不，"ab"和"ac"有'a'，但"ad"也有'a'？实际上'ab','ac','ad'公共前缀是'a'? 检查：所有第一个字符都是'a'，所以公共前缀是'a'? 等等，应该是'a'。这里需要明确。
            # 修正：["ab","ac","ad"] 公共前缀是 "a"，不是空。所以用另一个例子
            (["ab", "bc", "cd"], ""),
            (["prefix", "pref", "pre"], "pre"),  # 这是有公共前缀的，放在别的测试中
        ]
        # 提供真正无公共前缀的例子
        real_no_prefix = [
            (["abc", "bcd", "cde"], ""),
            (["hello", "world", "hi"], ""),
            (["a", "b", "c"], ""),
        ]
        for strs, expected in real_no_prefix:
            for name, func in self.algorithms:
                with self.subTest(strs=strs, algorithm=name):
                    self.assertEqual(func(strs), expected)

    def test_common_prefix_some_empty(self):
        """包含空字符串"""
        test_cases = [(["", "abc"], ""), (["abc", "", "def"], ""), (["", ""], "")]
        for strs, expected in test_cases:
            for name, func in self.algorithms:
                with self.subTest(strs=strs, algorithm=name):
                    self.assertEqual(func(strs), expected)

    def test_common_prefix_various_lengths(self):
        """不同长度的字符串，公共前缀为较短字符串"""
        test_cases = [
            (["flower", "flow", "flo"], "flo"),
            (["ab", "abc", "abcd"], "ab"),
            (["abcde", "abcd", "abc"], "abc"),
        ]
        for strs, expected in test_cases:
            for name, func in self.algorithms:
                with self.subTest(strs=strs, algorithm=name):
                    self.assertEqual(func(strs), expected)

    def test_common_prefix_with_single_char(self):
        """公共前缀为单个字符"""
        test_cases = [
            (["aab", "aac", "aad"], "aa"),  # 公共前缀"aa"不是单字符
            (["ab", "ac", "ad"], "a"),
            (["ba", "ca", "da"], ""),  # 无公共
        ]
        # 只保留有单个字符公共前缀的
        single_char = [(["ab", "ac", "ad"], "a")]
        for strs, expected in single_char:
            for name, func in self.algorithms:
                with self.subTest(strs=strs, algorithm=name):
                    self.assertEqual(func(strs), expected)

    def test_edge_empty_input(self):
        """空数组（约束说至少1个，但实现支持）"""
        # 根据函数实现，空数组应返回""
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func([]), "")

    def test_large_input(self):
        """性能测试（不严格，仅验证不崩溃）"""
        strs = ["a" * 200] * 200
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(strs), "a" * 200)


if __name__ == "__main__":
    unittest.main()
