import unittest
import random


class Solution(object):
    def addBinary(self, a, b):
        result = ""
        carry = 0
        index_a, index_b = len(a) - 1, len(b) - 1
        while index_a >= 0 and index_b >= 0:
            s = int(a[index_a]) + int(b[index_b]) + carry
            result = str(s % 2) + result
            carry = s // 2
            index_a -= 1
            index_b -= 1

        if index_a >= 0:
            while index_a >= 0:
                s = int(a[index_a]) + carry
                result = str(s % 2) + result
                carry = s // 2
                index_a -= 1
        elif index_b >= 0:
            while index_b >= 0:
                s = int(b[index_b]) + carry
                result = str(s % 2) + result
                carry = s // 2
                index_b -= 1

        if carry:
            result = "1" + result
        return result


class TestAddBinary(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # ---------- 基础用例 ----------
    def test_basic_1(self):
        self.assertEqual(self.sol.addBinary("11", "1"), "100")

    def test_basic_2(self):
        self.assertEqual(self.sol.addBinary("1010", "1011"), "10101")

    def test_basic_3(self):
        self.assertEqual(self.sol.addBinary("0", "0"), "0")

    def test_basic_4(self):
        self.assertEqual(self.sol.addBinary("1", "0"), "1")

    def test_basic_5(self):
        self.assertEqual(self.sol.addBinary("111", "111"), "1110")

    # ---------- 长度差异 ----------
    def test_len_diff_1(self):
        self.assertEqual(self.sol.addBinary("1", "111"), "1000")

    def test_len_diff_2(self):
        self.assertEqual(self.sol.addBinary("100", "1"), "101")

    def test_len_diff_3(self):
        self.assertEqual(self.sol.addBinary("1000", "1"), "1001")

    # ---------- 进位链 ----------
    def test_carry_propagation_1(self):
        self.assertEqual(self.sol.addBinary("1111", "1"), "10000")

    def test_carry_propagation_2(self):
        self.assertEqual(self.sol.addBinary("101010", "101010"), "1010100")

    def test_all_ones(self):
        self.assertEqual(self.sol.addBinary("1111111111", "1"), "10000000000")

    # ---------- 随机测试（对比 Python 内置 int 转换）----------
    def test_random_compare(self):
        for _ in range(100):
            # 随机生成长度 1~20 的二进制串
            len_a = random.randint(1, 20)
            len_b = random.randint(1, 20)
            a = "".join(random.choice("01") for _ in range(len_a))
            b = "".join(random.choice("01") for _ in range(len_b))

            expected = bin(int(a, 2) + int(b, 2))[2:]  # 去掉 '0b' 前缀
            self.assertEqual(self.sol.addBinary(a, b), expected)

    # ---------- 大长度测试 ----------
    def test_long_strings(self):
        a = "1" * 1000
        b = "1"
        expected = "1" + "0" * 1000
        self.assertEqual(self.sol.addBinary(a, b), expected)

        a = "1" * 500
        b = "1" * 500
        expected = "1" + "0" * 500
        self.assertEqual(self.sol.addBinary(a, b), expected)


if __name__ == "__main__":
    unittest.main()
