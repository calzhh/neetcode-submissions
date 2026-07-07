"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        current_rooms = 0 
        max_rooms = 0
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        
        i, j = 0, 0 

        while i < len(intervals):
            if start[i] < end[j]:
                current_rooms += 1
                i += 1
            else:
                current_rooms -= 1
                j += 1
            max_rooms = max(max_rooms, current_rooms)
        return max_rooms