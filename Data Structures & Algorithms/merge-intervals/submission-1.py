# a stack might be useful here
# keep adding
# if overlapping, pop and add new one

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort()

        for interval in intervals:
            if res:
                latestInterval = res[-1]

                print(latestInterval)
                print(interval)

                if (interval[1] <= latestInterval[1] or
                    (interval[0] >= latestInterval[0] and interval[0] <= latestInterval[1])
                ):
                    newInterval = [
                        min(interval[0], latestInterval[0]),
                        max(interval[1], latestInterval[1])
                    ]
                    res.pop()
                    res.append(newInterval)
                else:
                    res.append(interval)
            else:
                res.append(interval)

        return res