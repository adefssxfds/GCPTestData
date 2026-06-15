import unittest


# --- 将你的两个算法放在这里 ---
def length_of_longest_substring(s: str) -> int:
    char_map = {}
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


# --- 测试代码 ---
class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        # 统一管理两种求解算法
        self.substring_funcs = [
            length_of_longest_substring,
            length_of_longest_substring_set,
        ]

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)]
        for s, expected in test_cases:
            for func in self.substring_funcs:
                with self.subTest(func=func.__name__, s=s):
                    self.assertEqual(func(s), expected)

    def test_empty_string(self):
        """测试空字符串的情况"""
        s = ""
        expected = 0
        for func in self.substring_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(s), expected)

    def test_all_unique_characters(self):
        """测试所有字符都不相同的情况"""
        s = "abcdefg"
        expected = 7  # 整个字符串都是最长无重复子串
        for func in self.substring_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(s), expected)

    def test_all_same_characters(self):
        """测试所有字符都相同的情况"""
        s = "zzzzzz"
        expected = 1
        for func in self.substring_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(s), expected)

    def test_repeating_at_the_end(self):
        """测试重复字符出现在字符串末尾的情况"""
        s = "abcdxyzxyz"
        expected = 7  # "abcdxyz"
        for func in self.substring_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(s), expected)

    def test_repeating_at_the_beginning(self):
        """测试重复字符出现在字符串开头的情况"""
        s = "abcabc"
        expected = 3  # "abc"
        for func in self.substring_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(s), expected)

    def test_single_character(self):
        """测试单字符的情况"""
        s = "a"
        expected = 1
        for func in self.substring_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(s), expected)

    def test_mixed_characters_and_spaces(self):
        """测试包含空格和特殊字符的情况（符合约束条件）"""
        s = "a b c a b"
        expected = 5  # "a b c" (包含空格，长度为5)
        for func in self.substring_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(s), expected)


if __name__ == "__main__":
    unittest.main()
