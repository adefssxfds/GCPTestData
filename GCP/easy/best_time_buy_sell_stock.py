from typing import List
def max_profit(prices: List[int]) -> int:
    if not prices or len(prices) < 2:
        return 0
    
    min_price = prices[0]  # Minimum price seen so far
    max_profit_value = 0   # Maximum profit achievable so far
    
    # Iterate through prices starting from second day
    for price in prices[1:]:
        # Update maximum profit if selling today gives better profit
        max_profit_value = max(max_profit_value, price - min_price)
        
        # Update minimum price if today's price is lower
        min_price = min(min_price, price)
    
    return max_profit_value


def max_profit_brute_force(prices: List[int]) -> int:
    if not prices or len(prices) < 2:
        return 0
    
    max_profit_value = 0
    
    # Try all possible buy days
    for buy_day in range(len(prices) - 1):
        # Try all possible sell days after buy day
        for sell_day in range(buy_day + 1, len(prices)):
            profit = prices[sell_day] - prices[buy_day]
            max_profit_value = max(max_profit_value, profit)
    
    return max_profit_value


def max_profit_kadane_style(prices: List[int]) -> int:
    if not prices or len(prices) < 2:
        return 0
    
    max_profit_value = 0
    current_profit = 0
    
    # Calculate profit differences and apply Kadane's algorithm
    for i in range(1, len(prices)):
        daily_change = prices[i] - prices[i - 1]
        
        # Either extend current profit or start fresh
        current_profit = max(0, current_profit + daily_change)
        
        # Update maximum profit seen so far
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