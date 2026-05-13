class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = dict()
        for i in range(len(numbers)):
            if target - numbers[i] in map:
                return [map[target - numbers[i]]+1, i+1]
            else:
                map[numbers[i]] = i 
            print(map)    


        