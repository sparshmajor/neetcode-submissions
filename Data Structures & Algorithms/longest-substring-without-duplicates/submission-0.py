class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i = 0
        st =set() 
        for j in s:
            while j in st:
                st.remove(s[i])
                i+=1
            st.add(j)    
            res = max(res, len(st))   
        return res     








        