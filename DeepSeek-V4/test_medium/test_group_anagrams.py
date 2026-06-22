from typing import List, Dict
from collections import defaultdict
import unittest

# 方法1：排序法
def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups: Dict[str, List[str]] = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagram_groups[key].append(s)
    return list(anagram_groups.values())

# 方法2：字符计数法
def group_anagrams_counting(strs: List[str]) -> List[List[str]]:
    anagram_groups: Dict[tuple, List[str]] = defaultdict(list)
    for s in strs:
        char_count = [0] * 26
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        key = tuple(char_count)
        anagram_groups[key].append(s)
    return list(anagram_groups.values())

# 方法3：质数乘积法
def group_anagrams_prime(strs: List[str]) -> List[List[str]]:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    anagram_groups: Dict[int, List[str]] = defaultdict(list)
    for s in strs:
        key = 1
        for char in s:
            key *= primes[ord(char) - ord('a')]
        anagram_groups[key].append(s)
    return list(anagram_groups.values())


class TestGroupAnagrams(unittest.TestCase):
    def sort_result(self, res):
        """统一排序，消除内外层顺序影响，方便断言"""
        return sorted([sorted(g) for g in res])

    def test_example1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        expect = [["bat"],["nat","tan"],["ate","eat","tea"]]
        exp_sorted = self.sort_result(expect)
        
        self.assertEqual(self.sort_result(group_anagrams(strs)), exp_sorted)
        self.assertEqual(self.sort_result(group_anagrams_counting(strs)), exp_sorted)
        self.assertEqual(self.sort_result(group_anagrams_prime(strs)), exp_sorted)

    def test_example2_empty_str(self):
        strs = [""]
        expect = [[""]]
        self.assertEqual(group_anagrams(strs), expect)
        self.assertEqual(group_anagrams_counting(strs), expect)
        self.assertEqual(group_anagrams_prime(strs), expect)

    def test_example3_single_char(self):
        strs = ["a"]
        expect = [["a"]]
        self.assertEqual(group_anagrams(strs), expect)
        self.assertEqual(group_anagrams_counting(strs), expect)
        self.assertEqual(group_anagrams_prime(strs), expect)

    def test_all_same_group(self):
        strs = ["abc", "cba", "bca"]
        expect = [["abc", "cba", "bca"]]
        self.assertEqual(self.sort_result(group_anagrams(strs)), self.sort_result(expect))

    def test_no_anagram(self):
        strs = ["abc", "def", "ghi"]
        expect = [["abc"], ["def"], ["ghi"]]
        self.assertEqual(self.sort_result(group_anagrams(strs)), self.sort_result(expect))

if __name__ == '__main__':
    unittest.main()