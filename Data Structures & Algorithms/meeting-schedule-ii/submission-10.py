"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# first of all, sorting by start time would robably make life easier
# another way to ask this question is what's the max overlap of all the meeting times?
# for 2 meetings, we know meeting B overlaps IF ITS START IS BETWEEN THE START AND END OF THE PREVIOUS MEETING
# WITH SORTING, WE ARE GUARANTEED THAT START IS MORE THAN THE PREV START, IN THAT CASE JUST NEED TO KNOW IF THE START IS BEFORE THE PREV END
# one naive approachw ould be to go along the number line, and see how many meetings it belongs to, keeping a max counter
# 

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)