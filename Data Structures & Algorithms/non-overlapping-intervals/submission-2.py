# some useful functions would be figuring out where the overlaps are
# main thing to chew on here is that if you have a huge interval, you can either
# remove the smaller intervals in the middle, or obviously the big interval

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_int = sorted(intervals)

        prevEnd = sorted_int[0][1]
        res = 0

        for start, end in sorted_int[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)

        return res