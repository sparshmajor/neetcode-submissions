class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        result = float("inf")
        while l<=r:
            mid = l + (r-l)//2
            if nums[l] <= nums[mid]:
                result = min(result, nums[l])
                l =mid+1
            else:
                result = min(result, nums[mid])
                r= mid-1
        return result        



        