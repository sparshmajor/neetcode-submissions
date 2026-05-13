class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hms = dict()
        hmt = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hms[s[i]] = hms.get(s[i],0)+1
            hmt[t[i]] = hmt.get(t[i],0)+1
        for a,b in hms.items():
            if a not in hmt:
                return False
            else:
                if b != hmt[a]: 
                    return False
        return True                   






        