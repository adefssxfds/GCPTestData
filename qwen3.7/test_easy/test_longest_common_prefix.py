import unittest
from typing import List


# --- 将你的四个算法放在这里 ---
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


# --- 测试代码 ---
class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        # 统一管理四种求解算法，方便批量验证
        self.lcp_funcs = [
            longest_common_prefix,
            longest_common_prefix_horizontal,
            longest_common_prefix_divide_conquer,
            longest_common_prefix_trie,
        ]

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            (["flower", "flow", "flight"], "fl"),
            (["dog", "racecar", "car"], ""),
        ]
        for strs, expected in test_cases:
            for func in self.lcp_funcs:
                with self.subTest(func=func.__name__, strs=strs):
                    self.assertEqual(func(strs), expected)

    def test_single_string(self):
        """测试只有一个字符串的情况"""
        strs = ["single"]
        expected = "single"
        for func in self.lcp_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(strs), expected)

    def test_identical_strings(self):
        """测试所有字符串完全相同的情况"""
        strs = ["test", "test", "test"]
        expected = "test"
        for func in self.lcp_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(strs), expected)

    def test_empty_string_in_list(self):
        """测试列表中包含空字符串的情况，公共前缀必为空"""
        strs = ["abc", "", "abd"]
        expected = ""
        for func in self.lcp_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(strs), expected)

    def test_one_is_prefix_of_others(self):
        """测试其中一个字符串正好是其他字符串的前缀"""
        strs = ["pre", "prefix", "preparation"]
        expected = "pre"
        for func in self.lcp_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(strs), expected)

    def test_no_common_prefix(self):
        """测试首字母就不相同的情况"""
        strs = ["apple", "banana", "cherry"]
        expected = ""
        for func in self.lcp_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(strs), expected)


if __name__ == "__main__":
    unittest.main()
