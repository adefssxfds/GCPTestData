import unittest


# --- 将你的算法封装为 Solution 类（已修复缩进问题）---
class Solution(object):
    def letterCombinations(self, digits):
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        number = str(digits)

        if number == "":
            return []

        result = [""]
        for char in number:
            values = phoneMap[char]
            new_result = []
            # 修复了这里的缩进，确保嵌套循环逻辑正确
            for prefix in result:
                currElement = prefix
                for value in values:
                    new_result.append(currElement + value)
            result = new_result
        return result


# --- 测试代码 ---
class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
            ("2", ["a", "b", "c"]),
            ("", []),  # 补充测试空字符串的情况
        ]
        for digits, expected in test_cases:
            with self.subTest(digits=digits):
                result = self.solution.letterCombinations(digits)
                # 对结果和预期进行排序后比较，防止内部生成顺序差异导致断言失败
                self.assertEqual(sorted(result), sorted(expected))

    def test_single_digit(self):
        """测试单个数字的情况"""
        digits = "9"
        expected = ["w", "x", "y", "z"]
        result = self.solution.letterCombinations(digits)
        self.assertEqual(sorted(result), sorted(expected))

    def test_repeated_digits(self):
        """测试包含重复数字的情况"""
        digits = "22"
        expected = ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
        result = self.solution.letterCombinations(digits)
        self.assertEqual(sorted(result), sorted(expected))

    def test_max_length(self):
        """测试最大长度 (4位数字) 的情况"""
        digits = "234"
        expected = [
            "adg",
            "adh",
            "adi",
            "aeg",
            "aeh",
            "aei",
            "afg",
            "afh",
            "afi",
            "bdg",
            "bdh",
            "bdi",
            "beg",
            "beh",
            "bei",
            "bfg",
            "bfh",
            "bfi",
            "cdg",
            "cdh",
            "cdi",
            "ceg",
            "ceh",
            "cei",
            "cfg",
            "cfh",
            "cfi",
        ]
        result = self.solution.letterCombinations(digits)
        self.assertEqual(sorted(result), sorted(expected))

    def test_four_and_seven(self):
        """测试包含4个字母的数字(7和9)的情况"""
        digits = "79"
        expected = [
            "pw",
            "px",
            "py",
            "pz",
            "qw",
            "qx",
            "qy",
            "qz",
            "rw",
            "rx",
            "ry",
            "rz",
            "sw",
            "sx",
            "sy",
            "sz",
        ]
        result = self.solution.letterCombinations(digits)
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == "__main__":
    unittest.main()
