import unittest
from typing import List, Dict
from collections import defaultdict


# --- 将你的三个算法放在这里 ---
def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups: Dict[str, List[str]] = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        anagram_groups[key].append(s)
    return list(anagram_groups.values())


def group_anagrams_counting(strs: List[str]) -> List[List[str]]:
    anagram_groups: Dict[tuple, List[str]] = defaultdict(list)
    for s in strs:
        char_count = [0] * 26
        for char in s:
            char_count[ord(char) - ord("a")] += 1
        key = tuple(char_count)
        anagram_groups[key].append(s)
    return list(anagram_groups.values())


def group_anagrams_prime(strs: List[str]) -> List[List[str]]:
    primes = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
    ]
    anagram_groups: Dict[int, List[str]] = defaultdict(list)
    for s in strs:
        key = 1
        for char in s:
            key *= primes[ord(char) - ord("a")]
        anagram_groups[key].append(s)
    return list(anagram_groups.values())


# --- 测试代码 ---
class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        # 统一管理三种求解算法
        self.anagram_funcs = [
            group_anagrams,
            group_anagrams_counting,
            group_anagrams_prime,
        ]

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            (
                ["eat", "tea", "tan", "ate", "nat", "bat"],
                [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
            ),
            ([""], [[""]]),
            (["a"], [["a"]]),
        ]
        for strs, expected in test_cases:
            for func in self.anagram_funcs:
                with self.subTest(func=func.__name__, strs=strs):
                    result = func(strs)
                    # 对每个分组内部排序，再对整体结果排序，防止顺序差异导致断言失败
                    sorted_result = sorted([sorted(group) for group in result])
                    sorted_expected = sorted([sorted(group) for group in expected])
                    self.assertEqual(sorted_result, sorted_expected)

    def test_no_anagrams(self):
        """测试没有任何异位词的情况（所有单词都不同）"""
        strs = ["abc", "def", "ghi"]
        expected = [["abc"], ["def"], ["ghi"]]
        for func in self.anagram_funcs:
            with self.subTest(func=func.__name__):
                result = func(strs)
                sorted_result = sorted([sorted(group) for group in result])
                sorted_expected = sorted([sorted(group) for group in expected])
                self.assertEqual(sorted_result, sorted_expected)

    def test_all_anagrams(self):
        """测试所有单词都是异位词的情况"""
        strs = ["abc", "bca", "cab", "acb"]
        expected = [["abc", "bca", "cab", "acb"]]
        for func in self.anagram_funcs:
            with self.subTest(func=func.__name__):
                result = func(strs)
                sorted_result = sorted([sorted(group) for group in result])
                sorted_expected = sorted([sorted(group) for group in expected])
                self.assertEqual(sorted_result, sorted_expected)

    def test_empty_strings_and_single_chars(self):
        """测试空字符串与单字符混合的情况"""
        strs = ["", "", "a", "b", "a"]
        expected = [["", ""], ["a", "a"], ["b"]]
        for func in self.anagram_funcs:
            with self.subTest(func=func.__name__):
                result = func(strs)
                sorted_result = sorted([sorted(group) for group in result])
                sorted_expected = sorted([sorted(group) for group in expected])
                self.assertEqual(sorted_result, sorted_expected)

    def test_longer_anagrams(self):
        """测试较长字符串的异位词"""
        strs = ["listen", "silent", "enlist", "apple", "papel"]
        expected = [["listen", "silent", "enlist"], ["apple", "papel"]]
        for func in self.anagram_funcs:
            with self.subTest(func=func.__name__):
                result = func(strs)
                sorted_result = sorted([sorted(group) for group in result])
                sorted_expected = sorted([sorted(group) for group in expected])
                self.assertEqual(sorted_result, sorted_expected)


if __name__ == "__main__":
    unittest.main()
