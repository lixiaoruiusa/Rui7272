class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    @ DP Time: O(n), Space O(1) 
    keep looking min_price and max_profit 
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0
        
        min_price = max(prices)
        max_profit = 0
        
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > max_profit:
                max_profit = p - min_price
        
        return max_profit