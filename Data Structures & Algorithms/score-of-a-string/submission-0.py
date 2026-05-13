class Solution:
    def scoreOfString(self, s: str) -> int:
        i= 1
        res = 0
        while i < len(s):
            res += abs(ord(s[i-1]) - ord(s[i]))
            i+=1
        return res    
        