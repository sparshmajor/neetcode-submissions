import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap =[]
        for i, value in enumerate(arr):
            heapq.heappush(heap, (abs(x-value),value,i))
        pre_result=[]
        while(k):
            pre_result.append(heapq.heappop(heap))
            k-=1
        final_result =[]
        for val in sorted(pre_result, key=lambda x: x[2]):
            final_result.append(val[1]) 
        return final_result       




        