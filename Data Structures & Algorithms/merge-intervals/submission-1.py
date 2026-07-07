class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        print(intervals)
        res = [intervals[0]]
        i, j = 0, 1

        for start, end in intervals[1:]:
            prev_start = res[-1][0]
            prev_end = res[-1][1]

            if prev_end >= start:
                new_start = min(prev_start, start)
                new_end = max(prev_end, end)
                new_interval = [new_start, new_end]
                res.pop()
                res.append(new_interval)
            else:
                res.append([start, end])

        return res