class Solution:
    def maxProfit(self, prices: List[int]) -> int:            
        min_purchase = prices[0]
        max_profit = 0
        
        for i, val in enumerate(prices[1:]):
            temp = val - min_purchase
            if temp > max_profit:
                max_profit = temp
            
            if val < min_purchase:
                min_purchase = val
        
        return max_profit