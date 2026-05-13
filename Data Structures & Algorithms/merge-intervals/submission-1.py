# [[1,3],[1,5],[5,7], [8,9]]
# start = [1,3]
# i = [1,5]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res= []
        i = 0
        n = len(intervals)

        if n==1:
            return intervals
        n+=1    
        intervals.append([2000,2002])
        intervals.sort(key = lambda x : x[0])
        while i < n:
            print(i, res)
            print(intervals)
                
            while i+1 < n and intervals[i][1] < intervals[i+1][0]:
                print("dsssdd")
                res.append(intervals[i])
                i+=1
                continue
            new = intervals[i]
            flag =0
            while i+1 < n  and (intervals[i+1][0] <= new[1] ):
                flag =1
                new[0] = min(new[0], intervals[i+1][0])
                new[1] = max(new[1], intervals[i+1][1]) 
                i+=1
            if flag:
                res.append(new)    
            i+=1     
        return res         






        