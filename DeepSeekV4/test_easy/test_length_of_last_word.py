import unittest


# 假设两个函数已经定义（复制自题目）
def length_of_last_word(s: str) -> int:
    i = len(s) - 1
    while i >= 0 and s[i] == " ":
        i -= 1
    length = 0
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1
    return length


def length_of_last_word_split(s: str) -> int:
    return len(s.strip().split()[-1])


class TestLengthOfLastWord(unittest.TestCase):
    def setUp(self):
        # 两种待测试的实现
        self.functions = [
            ("手动遍历", length_of_last_word),
            ("split方法", length_of_last_word_split),
        ]

    def test_examples(self):
        """题目提供的三个示例"""
        test_cases = [
            ("Hello World", 5),
            ("   fly me   to   the moon  ", 4),
            ("luffy is still joyboy", 6),
        ]
        for s, expected in test_cases:
            for name, func in self.functions:
                with self.subTest(s=s, method=name):
                    self.assertEqual(func(s), expected)

    def test_single_word(self):
        """仅有一个单词，无空格"""
        test_cases = [("hello", 5), ("a", 1), ("abcde", 5)]
        for s, expected in test_cases:
            for name, func in self.functions:
                with self.subTest(s=s, method=name):
                    self.assertEqual(func(s), expected)

    def test_single_word_with_spaces(self):
        """单词前后有空格"""
        test_cases = [
            ("  hello  ", 5),
            ("   world", 5),
            ("python    ", 6),
            ("   code", 4),
        ]
        for s, expected in test_cases:
            for name, func in self.functions:
                with self.subTest(s=s, method=name):
                    self.assertEqual(func(s), expected)

    def test_multiple_words(self):
        """多个单词，中间多个空格"""
        test_cases = [
            ("a b c", 1),
            ("one   two   three", 5),
            ("  first  second  third  ", 5),
            ("apple banana cherry", 6),
            ("   extra    spaces   between   words", 5),
        ]
        for s, expected in test_cases:
            for name, func in self.functions:
                with self.subTest(s=s, method=name):
                    self.assertEqual(func(s), expected)

    def test_all_spaces_not_possible(self):
        """根据约束，至少有一个单词，所以不会全空格"""
        pass  # 不需要测试全空格

    def test_empty_string_not_allowed(self):
        """约束 s.length >= 1，但为了健壮性仍测试空字符串（如果允许）"""
        # 根据题目约束不会出现空字符串，但实现可能仍能处理
        # 此处不强制要求，但可测试确保不崩溃
        pass


if __name__ == "__main__":
    unittest.main()
