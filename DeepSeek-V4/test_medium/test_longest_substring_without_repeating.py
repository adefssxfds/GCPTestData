import unittest


# 两种滑动窗口实现
def length_of_longest_substring(s: str) -> int:
    char_map = {}
    start = 0
    max_length = 0
    for end, ch in enumerate(s):
        if ch in char_map and char_map[ch] >= start:
            start = char_map[ch] + 1
        char_map[ch] = end
        max_length = max(max_length, end - start + 1)
    return max_length


def length_of_longest_substring_set(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0
    for right, ch in enumerate(s):
        while ch in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(ch)
        max_length = max(max_length, right - left + 1)
    return max_length


# 暴力法（仅用于小规模验证）
def brute_force(s: str) -> int:
    n = len(s)
    max_len = 0
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
    return max_len


class TestLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.algorithms = [
            ("哈希表滑动窗口", length_of_longest_substring),
            ("集合滑动窗口", length_of_longest_substring_set),
        ]

    # ---------- 题目示例 ----------
    def test_example1(self):
        s = "abcabcbb"
        expected = 3
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(s), expected)

    def test_example2(self):
        s = "bbbbb"
        expected = 1
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(s), expected)

    def test_example3(self):
        s = "pwwkew"
        expected = 3
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(s), expected)

    # ---------- 边界情况 ----------
    def test_empty_string(self):
        s = ""
        expected = 0
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(s), expected)

    def test_single_char(self):
        s = "a"
        expected = 1
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(s), expected)

    def test_all_same_chars(self):
        s = "aaaaaa"
        expected = 1
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(s), expected)

    def test_unique_chars(self):
        s = "abcdefg"
        expected = 7
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(s), expected)

    def test_mixed_ascii(self):
        # 包含字母、数字、符号、空格
        s = "ab c!12ab c"
        # 最长无重复子串可能是 "ab c!12" (长度7) 或 "b c!12a" 等
        expected = 7
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(s), expected)

    # ---------- 随机测试（与暴力法对比，小规模）----------
    def test_random_compare(self):
        import random
        import string

        chars = string.ascii_letters + string.digits + string.punctuation + " "
        for _ in range(100):
            length = random.randint(0, 30)  # 小规模，暴力法可接受
            s = "".join(random.choice(chars) for __ in range(length))
            expected = brute_force(s)
            for name, func in self.algorithms:
                with self.subTest(algorithm=name, s=s):
                    self.assertEqual(func(s), expected)

    # ---------- 性能测试（大规模）----------
    def test_performance_long(self):
        import time

        # 构造一个长度为 50000 的字符串，交替重复，使得最长无重复子串长度有限
        s = (
            "abcdefghijklmnopqrstuvwxyz" * 2000
        )  # 26000 * 2? 实际长度 26*2000=52000，略超
        s = s[:50000]  # 截取到 50000
        start = time.time()
        result = length_of_longest_substring(s)
        elapsed = time.time() - start
        self.assertLess(elapsed, 1.0, f"滑动窗口耗时 {elapsed:.2f}s 超过1秒")
        # 结果应为 26（因为所有字母都有，无重复子串最长26）
        self.assertEqual(result, 26)

        # 全相同字符串
        s = "a" * 50000
        start = time.time()
        result = length_of_longest_substring(s)
        elapsed = time.time() - start
        self.assertLess(elapsed, 0.5)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
