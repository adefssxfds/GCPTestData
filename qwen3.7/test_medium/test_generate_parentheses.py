import unittest


# --- 将你的算法封装为 Solution 类 ---
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


# --- 测试代码 ---
class TestGenerateParenthesis(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
            (1, ["()"]),
        ]
        for n, expected in test_cases:
            with self.subTest(n=n):
                result = self.solution.generateParenthesis(n)
                # 对结果和预期进行排序后比较，防止内部生成顺序差异导致断言失败
                self.assertEqual(sorted(result), sorted(expected))

    def test_n_equals_2(self):
        """测试 n=2 的情况"""
        n = 2
        expected = ["(())", "()()"]
        result = self.solution.generateParenthesis(n)
        self.assertEqual(sorted(result), sorted(expected))

    def test_n_equals_4(self):
        """测试 n=4 的情况（验证更深层的递归与组合）"""
        n = 4
        expected = [
            "(((())))",
            "((()()))",
            "((())())",
            "((()))()",
            "(()(()))",
            "(()()())",
            "(()())()",
            "(())(())",
            "(())()()",
            "()((()))",
            "()(()())",
            "()(())()",
            "()()(())",
            "()()()()",
        ]
        result = self.solution.generateParenthesis(n)
        self.assertEqual(sorted(result), sorted(expected))

    def test_result_length(self):
        """验证生成的组合数量是否符合卡特兰数 (Catalan Number)"""
        # n=3 对应 5 种, n=4 对应 14 种, n=5 对应 42 种
        catalan_numbers = {3: 5, 4: 14, 5: 42}
        for n, expected_count in catalan_numbers.items():
            with self.subTest(n=n):
                result = self.solution.generateParenthesis(n)
                self.assertEqual(len(result), expected_count)

    def test_all_combinations_are_valid(self):
        """验证生成的所有字符串都是合法括号"""
        n = 5
        result = self.solution.generateParenthesis(n)
        for s in result:
            with self.subTest(s=s):
                # 简单的括号匹配验证逻辑
                balance = 0
                for char in s:
                    if char == "(":
                        balance += 1
                    elif char == ")":
                        balance -= 1
                    # 任何时刻右括号不能多于左括号
                    self.assertGreaterEqual(balance, 0, f"Invalid parenthesis: {s}")
                # 最终左右括号必须完全匹配
                self.assertEqual(balance, 0, f"Unbalanced parenthesis: {s}")


if __name__ == "__main__":
    unittest.main()
