import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k =k
        heapq.heapify(self.nums)
        while (len(self.nums) > k ):
            heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]    





# [1,2,3,3], k =3          
# [1,2,3,3,3] -> 3
# [1,2,3,3,3,5] -> 3  
# [1,2,3,3,3,5,6] -> 3      
# [1,2,3,3,3,5,6,7] -> 5      
# [1,2,3,3,3,5,6,7,8] -> 6      
