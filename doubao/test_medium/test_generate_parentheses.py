class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtracking(S, left, right):
            if len(S) == 2 * n:
                result.append(S)
                return 

            if left < n:
                backtracking(S+'(', left+1, right)

            if right < left:
                backtracking(S+')', left, right+1)

        backtracking('', 0, 0)
        return result


import unittest

class TestGenerateParenthesis(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # 示例 1: n = 3
    def test_n_3(self):
        res = self.sol.generateParenthesis(3)
        expect = ["((()))","(()())","(())()","()(())","()()()"]
        self.assertEqual(sorted(res), sorted(expect))

    # 示例 2: n = 1
    def test_n_1(self):
        self.assertEqual(self.sol.generateParenthesis(1), ["()"])

    # 额外用例: n = 2
    def test_n_2(self):
        res = self.sol.generateParenthesis(2)
        expect = ["(())", "()()"]
        self.assertEqual(sorted(res), sorted(expect))

    # 约束最大值 n = 8
    def test_n_8(self):
        res = self.sol.generateParenthesis(8)
        # 校验总数量（第8个卡特兰数）
        self.assertEqual(len(res), 429)

if __name__ == '__main__':
    unittest.main()