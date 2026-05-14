class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap =[]
        res=[]
        count =0
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i]*-1,i))
            count+=1
            if count == k:
                while heap[0][1] <= i-k:
                    heapq.heappop(heap)
                res.append(heap[0][0]*-1)
                count -=1
        return res