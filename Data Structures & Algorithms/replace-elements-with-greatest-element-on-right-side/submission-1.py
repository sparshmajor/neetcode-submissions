class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # brute force approach
        
        # res = []
        # for i, ele in enumerate(arr):
        #     if i+1 <= len(arr)-1:
        #         print(i)
        #         res.append(max(arr[i+1:]))
        # res.append(-1)    
        # return res  

        # O(n) solution
        n = len(arr)
        res = [0]*n
        rightMax= -1
        for i in range(n-1, -1, -1):
            res[i]=(rightMax)
            rightMax = max(rightMax, arr[i])
        return res    

