class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[1])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            prev_start = res[-1][0]
            prev_end = res[-1][1]

            if prev_end > start:
                pass
            else:
                res.append([start, end])

        return len(intervals) - len(res)