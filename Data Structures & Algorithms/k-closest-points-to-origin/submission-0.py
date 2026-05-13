import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res =[]
        for i in points:
            x1, x2 =i
            dis = math.sqrt(x1**2 + x2**2)
            heapq.heappush(minHeap, (dis, [x1,x2]))
        print(minHeap)    
        while k>0 :
            res.append(heapq.heappop(minHeap)[1])
            k-=1
        return res    



        