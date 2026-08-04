# easy case - between 2 intervals, prev.end < cur < next.start, then insert
# 

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        workingInterval = newInterval
        res = []

        for i in range(len(intervals)):
            if workingInterval[1] < intervals[i][0]:
                res.append(workingInterval)
                return res + intervals[i:]
            elif workingInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                workingInterval = [
                    min(workingInterval[0], intervals[i][0]),
                    max(workingInterval[1], intervals[i][1])
                ]

        res.append(workingInterval)

        return res
