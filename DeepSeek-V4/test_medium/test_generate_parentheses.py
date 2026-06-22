import unittest


class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtracking(S, left, right):
            if len(S) == 2 * n:
                result.append(S)
                return
            if left < n:
                backtracking(S + "(", left + 1, right)
            if right < left:
                backtracking(S + ")", left, right + 1)

        backtracking("", 0, 0)
        return result


class TestGenerateParenthesis(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # ---------- 题目示例 ----------
    def test_example1(self):
        n = 3
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        result = self.sol.generateParenthesis(n)
        # 顺序可能不同，排序后比较
        self.assertEqual(sorted(result), sorted(expected))

    def test_example2(self):
        n = 1
        expected = ["()"]
        self.assertEqual(self.sol.generateParenthesis(n), expected)

    # ---------- 边界情况 ----------
    def test_n_2(self):
        n = 2
        expected = ["(())", "()()"]
        result = self.sol.generateParenthesis(n)
        self.assertEqual(sorted(result), sorted(expected))

    def test_n_4(self):
        n = 4
        # 卡特兰数 C4 = 14，不逐一列举，只检查长度和有效性
        result = self.sol.generateParenthesis(n)
        self.assertEqual(len(result), 14)
        for s in result:
            self.assertTrue(self.is_valid_parentheses(s))

    def test_n_8(self):
        n = 8
        result = self.sol.generateParenthesis(n)
        # 卡特兰数 C8 = 1430
        self.assertEqual(len(result), 1430)
        for s in result:
            self.assertTrue(self.is_valid_parentheses(s))

    # 辅助函数：验证括号字符串是否有效
    def is_valid_parentheses(self, s):
        balance = 0
        for ch in s:
            if ch == "(":
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    # ---------- 随机与暴力枚举对比（小 n）----------
    def test_bruteforce_compare(self):
        import itertools

        def brute_force(n):
            # 生成所有长度为 2n 的括号组合，然后筛选有效的
            all_combinations = set()
            for seq in itertools.product("()", repeat=2 * n):
                s = "".join(seq)
                if self.is_valid_parentheses(s):
                    all_combinations.add(s)
            return sorted(all_combinations)

        for n in range(1, 5):
            expected = brute_force(n)
            result = sorted(self.sol.generateParenthesis(n))
            self.assertEqual(result, expected, f"Failed for n={n}")


if __name__ == "__main__":
    unittest.main()
