class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n
        ans = 1 
        while (l <=r ):
            mid = l+(r-l)//2
            # print("mid", mid)
            res = (mid * (mid+1))//2
            # print("res",res)
            if res > n:
                r = mid -1
            else:
                ans = mid
                l = mid + 1
        return ans        



        