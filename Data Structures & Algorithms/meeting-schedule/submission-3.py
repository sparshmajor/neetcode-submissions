"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        start = intervals[0]

        for i in intervals[1:]:
            if i.start <start.end and i.end >start.start:
                return False
            else:
                start = i    
        return True