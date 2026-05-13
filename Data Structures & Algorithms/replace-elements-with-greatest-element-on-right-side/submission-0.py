class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        for i, ele in enumerate(arr):
            if i+1 <= len(arr)-1:
                print(i)
                res.append(max(arr[i+1:]))
        res.append(-1)    
        return res    
