import unittest

class Solution(object):
    def letterCombinations(self, digits):
        phoneMap = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        if not digits:
            return []

        result = ['']
        for char in digits:
            values = phoneMap[char]
            new_result = []
            for prefix in result:
                for value in values:
                    new_result.append(prefix + value)
            result = new_result
        return result


class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # 示例1：两位数字
    def test_digits_23(self):
        digits = "23"
        expect = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertEqual(sorted(self.sol.letterCombinations(digits)), sorted(expect))

    # 示例2：单个数字
    def test_digits_2(self):
        digits = "2"
        expect = ["a","b","c"]
        self.assertEqual(self.sol.letterCombinations(digits), expect)

    # 边界：长度为4（题目最大约束）
    def test_max_length(self):
        digits = "27"
        res = self.sol.letterCombinations(digits)
        self.assertEqual(len(res), 3 * 4)

    # 数字7、9（4个字母特殊按键）
    def test_digit_7(self):
        digits = "7"
        self.assertEqual(self.sol.letterCombinations(digits), ["p","q","r","s"])

if __name__ == '__main__':
    unittest.main()