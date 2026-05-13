class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp ={}
        def solve(i, prev):
            if i >= len(nums):
                return 0
            if (i, prev) in dp:
                return dp[(i,prev)]    
            take = -float('inf')
            if prev ==-1 or nums[prev] < nums[i]:
                take = 1 + solve(i+1, i)
            no_take =  solve(i+1, prev)

            dp[(i, prev)]= max(take, no_take)
            return max(take, no_take)
        return solve(0, -1)    






        