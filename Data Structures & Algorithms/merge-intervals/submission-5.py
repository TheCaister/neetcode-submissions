# a stack might be useful here
# keep adding
# if overlapping, pop and add new one

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for interval in intervals:
            latestInterval = res[-1]

            if interval[0] <= latestInterval[1]:
                newInterval = [
                    min(interval[0], latestInterval[0]),
                    max(interval[1], latestInterval[1])
                ]
                res.pop()
                res.append(newInterval)
            else:
                res.append(interval)

        return res