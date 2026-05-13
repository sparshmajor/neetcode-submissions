import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num = nums#[-i for i in nums]
        heapq.heapify(num)
        x = len(nums) - k 
        while x:
            heapq.heappop(num)
            x-=1
        return heapq.heappop(num)

# 1,2,3,4,5 -> (5-2)         

        