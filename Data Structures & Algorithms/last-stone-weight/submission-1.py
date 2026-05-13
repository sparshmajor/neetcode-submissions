import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = [-i for i in stones]
        heapq.heapify(self.stones)
        while(len(self.stones)>1):
            x = abs(heapq.heappop(self.stones))
            y = abs(heapq.heappop(self.stones))
            print(x,y)
            e_max = max(x, y)
            e_min = min(x, y)
            res= e_max - e_min
            if res == 0:
                continue
            heapq.heappush(self.stones,-res)
        if len(self.stones) == 0:
            return 0    
        return abs(heapq.heappop(self.stones))        

        
