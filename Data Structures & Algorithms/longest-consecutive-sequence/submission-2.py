class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set= set(nums)
        seq_arr =[]
        res = 0 
        for i in nums:
            if i-1 not in hash_set:
                seq_arr.append(i)
        print(seq_arr)
        for num in seq_arr:
            cnt =0
            while num in hash_set:
                cnt+=1
                num += 1
            res= max(res, cnt)
        return res     