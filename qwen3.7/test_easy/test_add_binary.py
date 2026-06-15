import unittest


class Solution(object):
    def addBinary(self, a, b):
        result = ""

        carry = 0
        index_a, index_b = len(a) - 1, len(b) - 1
        while index_a >= 0 and index_b >= 0:
            result = str((int(a[index_a]) + int(b[index_b]) + carry) % 2) + result
            carry = (int(a[index_a]) + int(b[index_b]) + carry) // 2
            index_a -= 1
            index_b -= 1

        if index_a >= 0:
            while index_a >= 0:
                result = str((int(a[index_a]) + carry) % 2) + result
                carry = (int(a[index_a]) + carry) // 2
                index_a -= 1
        elif index_b >= 0:
            while index_b >= 0:
                result = str((int(b[index_b]) + carry) % 2) + result
                carry = (int(b[index_b]) + carry) // 2
                index_b -= 1

        if carry == 1:
            result = str(carry) + result
        return result


class TestAddBinary(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """测试题目示例1: 11 + 1 = 100"""
        self.assertEqual(self.solution.addBinary("11", "1"), "100")

    def test_example_2(self):
        """测试题目示例2: 1010 + 1011 = 10101"""
        self.assertEqual(self.solution.addBinary("1010", "1011"), "10101")

    def test_equal_length(self):
        """测试等长字符串相加: 101 + 110 = 1011"""
        self.assertEqual(self.solution.addBinary("101", "110"), "1011")

    def test_carry_to_new_digit(self):
        """测试最高位产生进位: 111 + 1 = 1000"""
        self.assertEqual(self.solution.addBinary("111", "1"), "1000")

    def test_single_digit(self):
        """测试单字符相加: 1 + 1 = 10"""
        self.assertEqual(self.solution.addBinary("1", "1"), "10")

    def test_zero_addition(self):
        """测试包含0的加法: 1010 + 0 = 1010"""
        self.assertEqual(self.solution.addBinary("1010", "0"), "1010")

    def test_leading_zeros(self):
        """测试包含前导零的情况: 001 + 01 = 10"""
        self.assertEqual(self.solution.addBinary("001", "01"), "10")


if __name__ == "__main__":
    unittest.main()
