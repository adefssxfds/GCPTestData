import unittest
import random
from typing import List

# 假设四个函数定义在这里（复制上面的代码）
# ...


class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        # 用于测试的典型用例
        self.test_cases = [
            ([7, 1, 5, 3, 6, 4], 5),
            ([7, 6, 4, 3, 1], 0),
            ([1, 2], 1),
            ([2, 1], 0),
            ([1, 2, 3, 4, 5], 4),
            ([5, 4, 3, 2, 1], 0),
            ([3, 3, 3, 3], 0),
            ([1], 0),
            ([10000, 0, 1, 2, 3], 3),
            ([0, 10000, 0, 10000], 10000),
        ]

    # ---------- 测试 max_profit (最优解) ----------
    def test_max_profit(self):
        for prices, expected in self.test_cases:
            with self.subTest(prices=prices):
                self.assertEqual(max_profit(prices), expected)

    # ---------- 测试暴力法 ----------
    def test_brute_force(self):
        for prices, expected in self.test_cases:
            with self.subTest(prices=prices):
                self.assertEqual(max_profit_brute_force(prices), expected)

    # ---------- 测试 Kadane 风格 ----------
    def test_kadane_style(self):
        for prices, expected in self.test_cases:
            with self.subTest(prices=prices):
                self.assertEqual(max_profit_kadane_style(prices), expected)

    # ---------- 测试返回索引的函数 ----------
    def test_with_indices(self):
        # 普通获利情况
        profit, buy, sell = max_profit_with_indices([7, 1, 5, 3, 6, 4])
        self.assertEqual(profit, 5)
        self.assertEqual(buy, 1)  # 价格为 1
        self.assertEqual(sell, 4)  # 价格为 6

        # 无获利情况
        profit, buy, sell = max_profit_with_indices([5, 4, 3, 2, 1])
        self.assertEqual(profit, 0)
        self.assertEqual(buy, -1)
        self.assertEqual(sell, -1)

        # 单个元素
        profit, buy, sell = max_profit_with_indices([42])
        self.assertEqual(profit, 0)
        self.assertEqual(buy, -1)
        self.assertEqual(sell, -1)

        # 提前出现更低价格但之后更高利润的情况
        profit, buy, sell = max_profit_with_indices([10, 1, 2, 20, 3])
        self.assertEqual(profit, 19)  # 1 买入，20 卖出
        self.assertEqual(buy, 1)
        self.assertEqual(sell, 3)

    # ---------- 随机测试：四种方法结果应一致 ----------
    def test_random_consistency(self):
        for _ in range(100):
            # 生成长度 1~30 的随机价格数组
            n = random.randint(1, 30)
            prices = [random.randint(0, 100) for _ in range(n)]
            p1 = max_profit(prices)
            p2 = max_profit_brute_force(prices)
            p3 = max_profit_kadane_style(prices)
            p4, _, _ = max_profit_with_indices(prices)
            self.assertEqual(p1, p2, f"Failed for {prices}")
            self.assertEqual(p1, p3, f"Failed for {prices}")
            self.assertEqual(p1, p4, f"Failed for {prices}")

    # ---------- 性能测试（不严格断言，只确保不超时）----------
    def test_large_performance(self):
        # 构造 10^5 长度的数组（递减序列，最大利润 0）
        prices = list(range(100000, 0, -1))
        # 期望快速返回
        self.assertEqual(max_profit(prices), 0)
        # Kadane 风格也应快速返回
        self.assertEqual(max_profit_kadane_style(prices), 0)


if __name__ == "__main__":
    unittest.main()
