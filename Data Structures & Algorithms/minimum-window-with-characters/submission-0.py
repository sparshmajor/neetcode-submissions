class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counT, window = {}, {}
        for c in t:
            counT[c] = counT.get(c, 0) + 1

        have , need =0, len(counT)
        l=0
        reslen = float("inf")
        res=[-1,-1]
        for r in range(len(s)):
            c= s[r]
            window[c] = 1+ window.get(c,0)

            if c in counT and window[c] == counT[c]:
                have+=1

            while have == need:
                if (r-l+1) < reslen:
                    reslen = r-l+1
                    res = [l,r]
                window[s[l]]-=1
                if s[l] in counT and window[s[l]] < counT[s[l]]:
                    have -=1
                l+=1
        l, r = res
        return s[l : r + 1] if reslen != float("infinity") else ""        











        