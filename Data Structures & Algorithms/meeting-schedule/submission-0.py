"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        i, j = 0, 1
        n = len(intervals)

        while j < n:
            if intervals[i].end > intervals[j].start:
                # [(0,30),(5,10),(15,20)]
                # 30 > 5 = overlap 
                return False
            else:
                i += 1
                j += 1
        return True
            