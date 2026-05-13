class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        prefix =0
        sufix = 0
        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            sufix = nums[len(nums)-1-i] * (sufix or 1)
            res = max(res, prefix, sufix)
        return res    



        