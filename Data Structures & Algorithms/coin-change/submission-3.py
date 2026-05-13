class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        res= float('inf')
        dp = {}
        def solve(coins, amt):
            nonlocal res
            if amt ==0:
                return 0
            if amt in dp:
                return dp[amt]    
            res = float('inf')
            for i in coins:
                if amt-i >= 0:
                    res = min(res, 1+ solve(coins, amt-i))
            dp[amt] = res        
            return res        
        solve(coins, amount)            
        return -1 if res == float('inf') else res          



        