# 121. Best Time to Buy and Sell Stock - Easy

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# The solution is in Python 3

def maxProfit(prices: list[int]) -> int:
    # 1. set a buying price and profit is zero initially in any investment
    profit = 0
    buy = prices[0]

    for price in prices[1:]:
        # 2. check if the new price is lesser than buying price then buy it
        if price < buy: 
            buy = price
        # 3. check if profit is more from the new sale then change the profit but keep it maxx!
        elif price - buy > profit:
            profit = max(profit, price - buy)
    return profit