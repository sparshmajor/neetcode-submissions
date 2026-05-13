import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res= r
        while l<=r:
            print(l,r)
            mid = (l+r)//2
            print("mid", mid)
            x= 0
            for i in piles:
                x+=math.ceil(i/mid)
                
            print("x",x) 
            if x<=h:
                res = mid
                r = mid-1 
            else:
                l = mid+1
            print("res",res)    
        return res                  


        