class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        result is always going to present between 1 and len(nums)
        """
        #brute force
        # set_nums = set(nums)
        # for i in range(len(nums)+1):
        #     if i+1 in set_nums:
        #         continue
        #     else:
        #         return i+1
        
        #binary nums
        nums.sort()
        def binary_nums(x):
            l = 0
            r = len(nums)-1
            while (l<=r):
                mid = (l+r)//2
                if x > nums[mid]:
                    l = mid+1
                elif x <  nums[mid]:
                    r = mid-1
                else:
                    return True
            return False
        for i in range(0,len(nums)+1):
            if not binary_nums(i+1):
                return i+1









        
        