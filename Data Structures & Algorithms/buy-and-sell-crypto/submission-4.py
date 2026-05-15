class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        lowest = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            
            current = prices[i] - lowest
            if current > profit:
                profit = current
        return profit