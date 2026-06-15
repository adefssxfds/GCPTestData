import unittest


# --- 将你的两个算法放在这里 ---
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


# --- 测试代码 ---
class TestLengthOfLastWord(unittest.TestCase):
    def setUp(self):
        # 统一管理两种求解方法，方便批量验证
        self.funcs = [length_of_last_word, length_of_last_word_split]

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            ("Hello World", 5),
            ("   fly me   to   the moon  ", 4),
            ("luffy is still joyboy", 6),
        ]
        for s, expected in test_cases:
            for func in self.funcs:
                with self.subTest(func=func.__name__, s=s):
                    self.assertEqual(func(s), expected)

    def test_trailing_spaces(self):
        """测试包含大量尾部空格的情况"""
        s = "hello     "
        expected = 5
        for func in self.funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(s), expected)

    def test_multiple_spaces_between(self):
        """测试单词之间有极多空格的情况"""
        s = "a    b    c"
        expected = 1
        for func in self.funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(s), expected)

    def test_single_word(self):
        """测试只有一个单词的情况"""
        s = "SingleWord"
        expected = 10
        for func in self.funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(s), expected)

    def test_single_word_with_trailing_spaces(self):
        """测试单个单词且带有尾部空格"""
        s = "Word   "
        expected = 4
        for func in self.funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(s), expected)

    def test_leading_spaces(self):
        """测试带有前导空格的情况"""
        s = "   leading"
        expected = 7
        for func in self.funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(s), expected)


if __name__ == "__main__":
    unittest.main()
