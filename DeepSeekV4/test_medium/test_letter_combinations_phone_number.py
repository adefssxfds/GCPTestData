import unittest
from typing import List, Dict
from collections import defaultdict


# 三种实现（复制自题目）
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


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.algorithms = [
            ("排序", group_anagrams),
            ("计数", group_anagrams_counting),
            ("质数乘积", group_anagrams_prime),
        ]

    def normalize(self, groups):
        """将结果标准化：每组内排序，整体排序，便于比较"""
        return sorted([sorted(group) for group in groups])

    def test_example1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        expected_norm = self.normalize(expected)
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                result = func(strs)
                self.assertEqual(self.normalize(result), expected_norm)

    def test_example2(self):
        strs = [""]
        expected = [[""]]
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                result = func(strs)
                self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_example3(self):
        strs = ["a"]
        expected = [["a"]]
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                result = func(strs)
                self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_empty_strings(self):
        strs = ["", "", ""]
        expected = [["", "", ""]]
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                result = func(strs)
                self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_single_character_anagrams(self):
        strs = ["a", "b", "a", "c", "b"]
        expected = [["a", "a"], ["b", "b"], ["c"]]
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                result = func(strs)
                self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_long_strings(self):
        strs = ["abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"]
        expected = [["abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"]]
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                result = func(strs)
                self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_no_anagrams(self):
        strs = ["abc", "def", "ghi"]
        expected = [["abc"], ["def"], ["ghi"]]
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                result = func(strs)
                self.assertEqual(self.normalize(result), self.normalize(expected))

    # 随机测试，对比三种实现结果是否一致
    def test_random_consistency(self):
        import random
        import string

        for _ in range(100):
            length = random.randint(0, 20)
            strs = []
            for _ in range(length):
                # 随机生成长度 0~10 的字符串
                s_len = random.randint(0, 10)
                s = "".join(random.choices(string.ascii_lowercase, k=s_len))
                strs.append(s)
            results = []
            for name, func in self.algorithms:
                result = func(strs)
                # 标准化后比较
                norm = self.normalize(result)
                results.append(norm)
            # 所有结果应相同
            for i in range(1, len(results)):
                self.assertEqual(
                    results[0],
                    results[i],
                    f"Mismatch between algorithms for input {strs}",
                )

    # 性能测试（仅确保不超时）
    def test_performance(self):
        import time

        strs = [
            "".join(sorted("abcdefghijklmnopqrstuvwxyz"[: i % 26]))
            for i in range(10000)
        ]
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                start = time.time()
                result = func(strs)
                elapsed = time.time() - start
                # 期望在合理时间内完成（例如 2 秒）
                self.assertLess(elapsed, 2.0, f"{name} took {elapsed:.2f}s")


if __name__ == "__main__":
    unittest.main()
