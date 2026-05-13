class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = nums[0]
        res= (0,0)
        count =0
        for i in nums:
            # print(i, count, res)
            if i == n:
                count +=1
            else:
                n = i
                count=1    
            if count > len(nums)//2:
                # print("hbdjhf")
                if count > res[0]:
                    res = (count, i)
        return res[1]                  

        