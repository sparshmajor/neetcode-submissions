class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res= 0
        for i in nums:
            ans =1
            l = i-1
            r = i+1
            while l in st:
                ans+=1
                st.remove(l)
                l-=1
            while r in st:
                ans+=1
                st.remove(r)
                r+=1
            res= max(res, ans)   
        return res         


        