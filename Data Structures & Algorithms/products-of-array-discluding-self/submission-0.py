class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res= [1]*len(nums)
        res2=[1]*len(nums)
        final_res=[]
        prefix =1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix*nums[i]
        print("prefix", res)
        sufix =1
        for i in range(len(nums)-1,-1,-1):
            res2[i] = sufix
            sufix = sufix*nums[i]
        print("sufix", res2)
        for i, j in zip(res, res2):
            final_res.append(i*j)
        return final_res

