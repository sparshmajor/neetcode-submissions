class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        result is always going to present between 1 and len(nums)
        """
        #brute force
        set_nums = set(nums)
        for i in range(len(nums)+1):
            if i+1 in set_nums:
                continue
            else:
                return i+1

        
        