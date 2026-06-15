from best_time_buy_sell_stock import (max_profit, max_profit_brute_force,
                                      max_profit_kadane_style, max_profit_with_indices)

from best_time_buy_sell_stock import *

def test_max_profit():
    # Test case 1: Example from the problem statement
    assert max_profit([7,1,5,3,6,4]) == 5

    # Test case 2: No profit possible
    assert max_profit([7,6,4,3,1]) == 0

    # Test case 3: Consecutive days with no profit
    assert max_profit([4,3,2,1]) == 0

def test_max_profit_brute_force():
    # Test case 1: Example from the problem statement
    assert max_profit_brute_force([7,1,5,3,6,4]) == 5

    # Test case 2: No profit possible
    assert max_profit_brute_force([7,6,4,3,1]) == 0

    # Test case 3: Consecutive days with no profit
    assert max_profit_brute_force([4,3,2,1]) == 0

def test_max_profit_kadane_style():
    # Test case 1: Example from the problem statement
    assert max_profit_kadane_style([7,1,5,3,6,4]) == 5

    # Test case 2: No profit possible
    assert max_profit_kadane_style([7,6,4,3,1]) == 0

    # Test case 3: Consecutive days with no profit
    assert max_profit_kadane_style([4,3,2,1]) == 0

def test_max_profit_with_indices():
    # Test case 1: Example from the problem statement
    assert max_profit_with_indices([7,1,5,3,6,4]) == (5, 2, 5)

    # Test case 2: No profit possible
    assert max_profit_with_indices([7,6,4,3,1]) == (0, -1, -1)

    # Test case 3: Consecutive days with no profit
    assert max_profit_with_indices([4,3,2,1]) == (0, -1, -1)

# ===== 补充测试（迭代优化） =====

def test_max_profit_empty_list():
    assert max_profit([]) == 0, "Should return 0 for empty list"


def test_max_profit_single_price():
    assert max_profit([1]) == 0, "Should return 0 for single price"

# 测试函数 max_profit_brute_force

def test_max_profit_brute_force_empty_list():
    assert max_profit_brute_force([]) == 0, "Should return 0 for empty list"


def test_max_profit_brute_force_single_price():
    assert max_profit_brute_force([1]) == 0, "Should return 0 for single price"

# 测试函数 max_profit_kadane_style

def test_max_profit_kadane_style_empty_list():
    assert max_profit_kadane_style([]) == 0, "Should return 0 for empty list"


def test_max_profit_kadane_style_single_price():
    assert max_profit_kadane_style([1]) == 0, "Should return 0 for single price"

# 测试函数 max_profit_with_indices

def test_max_profit_with_indices_empty_list():
    assert max_profit_with_indices([]) == (0, -1, -1), "Should return (0, -1, -1) for empty list"


def test_max_profit_with_indices_single_price():
    assert max_profit_with_indices([1]) == (0, -1, -1), "Should return (0, -1, -1) for single price"
