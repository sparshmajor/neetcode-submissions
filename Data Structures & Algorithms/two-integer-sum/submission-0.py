class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = dict()
        for i in range(len(nums)):
            n = nums[i]
            if target-n in hmap:
                return [hmap[target-n], i]

            hmap[n] = i



        