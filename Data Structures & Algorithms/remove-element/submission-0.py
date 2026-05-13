class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i =0
        ori_len = len(nums)
        while i < ori_len:
            if nums[i] == val:
                count +=1
                x= nums[i]
                del nums[i]
                nums.append(x)
                ori_len -=1
            else:
                i+=1      
        return len(nums) - count       



        