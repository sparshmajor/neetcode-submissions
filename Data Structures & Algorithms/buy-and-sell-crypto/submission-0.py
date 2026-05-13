class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        buy = float('inf')
        profit = 0
        while( i < len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            profit = max(profit, prices[i]-buy)     
            i+=1
        return profit    

        