class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = dict()
        count =0
        res =[]
        for i in nums:
            map[i] = map.get(i,0)+1
        mapped = list(map.items())
        mapped.sort(key = lambda x: x[1])

        for a, b in mapped[::-1]:
            res.append(a)
            count+=1
            if count == k:
                break
            
        
        return res 




        