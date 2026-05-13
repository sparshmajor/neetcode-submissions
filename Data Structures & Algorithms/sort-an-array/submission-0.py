class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #merge sort
        def partition(l, r):
            if l < r:
                mid = l + (r - l) // 2
                partition(l, mid)
                partition(mid+1, r)
                merge(l, mid, r)

        def merge(l,mid,r):
            result = []
            i = l
            j = mid+1
            while(i <= mid and j<= r):
                if nums[i] < nums[j]:
                    result.append(nums[i])
                    i+=1
                else:
                    result.append(nums[j])
                    j+=1
            while(i<= mid):
                result.append(nums[i])
                i+=1
            while(j<= r):
                result.append(nums[j])
                j+=1
            
            nums[l:r + 1] = result


        partition(0, len(nums)-1)
        return nums  