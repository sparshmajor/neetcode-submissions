"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_array = []
        end_array = []
        for i in intervals:
            start_array.append(i.start)
            end_array.append(i.end)
        start_array.sort()
        end_array.sort()
        i=0
        j=0
        count = 0
        res = -1
        while(i< len(start_array) and j < len(end_array)):
            if start_array[i] < end_array[j]:
                count+=1
                res = max(res, count)
                i+=1
            else:
                count-=1 
                j+=1     
        return res if res >0 else 0          
            






        