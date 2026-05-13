class Solution:
    def recursive(self, nums,l, r, target):
        if l <= r:
            mid = l+(r-l)//2
            if nums[mid] < target:
                return self.recursive(nums, mid+1, r, target)
            elif nums[mid] > target:
                return self.recursive(nums, l, mid-1, target)
            else:
                return mid    
        else:
            return -1        




    def search(self, nums: List[int], target: int) -> int:
        #iterative solution
        # l = 0
        # r = len(nums)-1
        # res=-1
        # while(l<=r):
        #     mid = l + (r-l)//2
        #     if nums[mid] > target:
        #         r = mid-1
        #     elif nums[mid] < target:
        #         l = mid+1
        #     else:
        #         return mid
        # return res

        #recursive solution
        return self.recursive(nums, 0, len(nums)-1, target)
        
