from typing import List

def maxProfit(prices: List[int]) -> int:
    max_profit : int = 0
    buying_price : int = prices[0]
    for current_price in prices:
        if current_price < buying_price:
            buying_price = current_price
        profit : int = current_price - buying_price
        if profit > max_profit:
            max_profit = profit
    return max_profit
    
prices = [7,6,4,3,1]
print(maxProfit(prices))

# prices : int
# if prices is None:
#     print("hurray")