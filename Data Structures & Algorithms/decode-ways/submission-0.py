class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def solve(i, st):
            if i == len(st) :
                return 1
            if st[i] == '0':
                return 0    
            if i in dp:
                return dp[i]    
            res= solve(i+1, st)
            if i+1 < (len(st)) and (st[i] == '1' or (st[i]=='2' and st[i+1] in '0123456')):
                res+=solve(i+2,st)
            dp[i] = res
            return res
        return solve(0, s)        

        