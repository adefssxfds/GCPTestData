import unittest
from typing import List


# --- 将你的四个函数放在这里 ---
def max_profit(prices: List[int]) -> int:
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit_value = 0

    for price in prices[1:]:
        max_profit_value = max(max_profit_value, price - min_price)
        min_price = min(min_price, price)

    return max_profit_value


def max_profit_brute_force(prices: List[int]) -> int:
    if not prices or len(prices) < 2:
        return 0

    max_profit_value = 0

    for buy_day in range(len(prices) - 1):
        for sell_day in range(buy_day + 1, len(prices)):
            profit = prices[sell_day] - prices[buy_day]
            max_profit_value = max(max_profit_value, profit)

    return max_profit_value


def max_profit_kadane_style(prices: List[int]) -> int:
    if not prices or len(prices) < 2:
        return 0

    max_profit_value = 0
    current_profit = 0

    for i in range(1, len(prices)):
        daily_change = prices[i] - prices[i - 1]
        current_profit = max(0, current_profit + daily_change)
        max_profit_value = max(max_profit_value, current_profit)

    return max_profit_value


def max_profit_with_indices(prices: List[int]) -> tuple[int, int, int]:
    if not prices or len(prices) < 2:
        return (0, -1, -1)

    min_price = prices[0]
    min_price_index = 0
    max_profit_value = 0
    best_buy_day = -1
    best_sell_day = -1

    for i in range(1, len(prices)):
        current_profit = prices[i] - min_price

        if current_profit > max_profit_value:
            max_profit_value = current_profit
            best_buy_day = min_price_index
            best_sell_day = i

        if prices[i] < min_price:
            min_price = prices[i]
            min_price_index = i

    return (max_profit_value, best_buy_day, best_sell_day)


# --- 测试代码 ---
class TestMaxProfit(unittest.TestCase):
    """测试返回最大利润的三个核心函数"""

    def setUp(self):
        # 将三个返回利润的函数放入列表，方便统一测试
        self.profit_funcs = [
            max_profit,
            max_profit_brute_force,
            max_profit_kadane_style,
        ]

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)]
        for prices, expected in test_cases:
            for func in self.profit_funcs:
                with self.subTest(func=func.__name__, prices=prices):
                    self.assertEqual(func(prices), expected)

    def test_monotonic_increasing(self):
        """测试单调递增数组"""
        prices = [1, 2, 3, 4, 5]
        expected = 4  # 5 - 1
        for func in self.profit_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(prices), expected)

    def test_single_element(self):
        """测试只有一个元素的边界情况"""
        prices = [5]
        for func in self.profit_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(prices), 0)

    def test_empty_list(self):
        """测试空列表"""
        prices = []
        for func in self.profit_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(prices), 0)

    def test_with_zeros(self):
        """测试包含0的价格"""
        prices = [0, 5, 0, 10]
        expected = 10  # 10 - 0
        for func in self.profit_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(prices), expected)


class TestMaxProfitWithIndices(unittest.TestCase):
    """专门测试返回利润及买卖日期的函数"""

    def test_basic_indices(self):
        """测试示例1的索引"""
        prices = [7, 1, 5, 3, 6, 4]
        expected = (5, 1, 4)  # 利润5, 买入日1, 卖出日4
        self.assertEqual(max_profit_with_indices(prices), expected)

    def test_no_profit_indices(self):
        """测试无法获利时的索引"""
        prices = [7, 6, 4, 3, 1]
        expected = (0, -1, -1)
        self.assertEqual(max_profit_with_indices(prices), expected)

    def test_monotonic_increasing_indices(self):
        """测试单调递增的索引"""
        prices = [1, 2, 3, 4, 5]
        expected = (4, 0, 4)  # 利润4, 买入日0, 卖出日4
        self.assertEqual(max_profit_with_indices(prices), expected)

    def test_single_element_indices(self):
        """测试单元素的索引"""
        prices = [5]
        expected = (0, -1, -1)
        self.assertEqual(max_profit_with_indices(prices), expected)


if __name__ == "__main__":
    unittest.main()
