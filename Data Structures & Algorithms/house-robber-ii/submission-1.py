class Solution:
    def rob_sol(self, nums, memo, i):
        if i in memo:
            return memo[i]
        if i >= len(nums):
            return 0     

        take = nums[i] + self.rob_sol(nums, memo, i+2)
        n_take =  self.rob_sol(nums, memo, i+1)
        memo[i]= max(take, n_take)
        return memo[i]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        a = self.rob_sol(nums[:-1], {}, 0)
        b = self.rob_sol(nums[1:], {}, 0)
        return max(a,b)

        