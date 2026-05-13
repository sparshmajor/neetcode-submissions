class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        map = {}
        while(i<len(nums)):
            if nums[i] in map and abs(map[nums[i]]-i)<=k:
                return True
            map[nums[i]]=i
            i+=1
        return False    




                
        