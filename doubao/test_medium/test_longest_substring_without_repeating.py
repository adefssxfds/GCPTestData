from typing import Dict
import unittest

def length_of_longest_substring(s: str) -> int:
    char_map: Dict[str, int] = {}
    start = 0
    max_length = 0
    for end in range(len(s)):
        current_char = s[end]
        if current_char in char_map and char_map[current_char] >= start:
            start = char_map[current_char] + 1
        char_map[current_char] = end
        max_length = max(max_length, end - start + 1)
    return max_length

def length_of_longest_substring_set(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

class TestLongestSubstring(unittest.TestCase):
    def test_cases(self):
        test_data = [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
            ("", 0),
            (" ", 1),
            ("au", 2),
            ("abba", 2),
            ("123 456!", 7)
        ]
        for s, expect in test_data:
            with self.subTest(s=s):
                self.assertEqual(length_of_longest_substring(s), expect)
                self.assertEqual(length_of_longest_substring_set(s), expect)

if __name__ == '__main__':
    unittest.main()