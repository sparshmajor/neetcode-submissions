class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_cut(nums):
            result = [float("inf"), -1]
            l=0
            r=len(nums)-1
            while l<=r:
                mid = l + (r-l)//2
                if nums[l] <= nums[mid]:
                    if nums[l] < result[0]:
                        result[0] = nums[l]
                        result[1] = l 
                    l = mid+1
                else:
                    if nums[mid] < result[0]:
                        result[0] = nums[mid]
                        result[1] = mid
                    r= mid-1
            return result[1]        

        def binary_search(arr,l,r, target):
            while l<r:
                mid = l+(r-l)//2
                if target <= arr[mid]:
                    r= mid
                else:
                    l =mid+1
            return l if arr[l] == target else -1
        
        cut = find_cut(nums)
        print(cut)
        ans= binary_search(nums,0,cut, target)
        print("first", ans)
        if ans != -1:
            return ans
        ans =  binary_search(nums,cut,len(nums)-1, target)  
        print("second", ans)
        return ans



