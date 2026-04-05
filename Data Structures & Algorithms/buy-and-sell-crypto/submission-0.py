class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            current_profit = price - lowest
            if current_profit > max_profit:
                max_profit = current_profit
        return max_profit