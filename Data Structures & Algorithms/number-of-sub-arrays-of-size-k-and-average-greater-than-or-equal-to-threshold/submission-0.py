class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        j = k-1
        res = 0
        while(j< len(arr)):
            if sum(arr[i:j+1])//k >= threshold:
                res+=1
            i+=1
            j+=1
        return res         

        