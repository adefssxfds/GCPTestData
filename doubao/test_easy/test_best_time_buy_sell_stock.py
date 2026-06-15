from typing import List


# 原有四个实现函数
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


# 测试代码
if __name__ == "__main__":
    # 测试用例：(价格数组, 预期最大利润)
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),  # 示例1
        ([7, 6, 4, 3, 1], 0),  # 示例2，持续下跌无利润
        ([1], 0),  # 长度为1
        ([2, 1], 0),  # 两天下跌
        ([1, 2], 1),  # 两天上涨
        ([3, 2, 6, 5, 0, 3], 4),  # 常规多波动
        ([0, 0, 0, 0], 0),  # 价格全相同
    ]

    func_list = [
        ("贪心单遍历", max_profit),
        ("暴力枚举", max_profit_brute_force),
        ("Kadane算法", max_profit_kadane_style),
    ]

    print("===== 股票最大利润 测试开始 =====\n")
    all_pass = True

    for idx, (prices, expect) in enumerate(test_cases, 1):
        print(f"【测试用例 {idx}】prices = {prices}, 预期利润 = {expect}")
        # 测试三个返回纯利润的函数
        for name, func in func_list:
            res = func(prices)
            status = "✅ 通过" if res == expect else "❌ 失败"
            if res != expect:
                all_pass = False
            print(f"  {name}: 输出 = {res} | {status}")

        # 测试带下标版本
        profit, buy_idx, sell_idx = max_profit_with_indices(prices)
        status_idx = "✅ 通过" if profit == expect else "❌ 失败"
        if profit != expect:
            all_pass = False
        print(
            f"  带下标版本: 利润={profit}, 买入日={buy_idx}, 卖出日={sell_idx} | {status_idx}\n"
        )

    print("===== 全部测试结果汇总 =====")
    print("所有用例全部通过" if all_pass else "存在用例测试失败")
