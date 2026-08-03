# sort intervals, then find the first occurrence.... hold on I don't think that's gonna work
# 

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sorted_interv = sorted(intervals)
        minHeap = []

        res, interv_index = {}, 0

        for q in sorted(queries):
            while interv_index < len(sorted_interv) and sorted_interv[interv_index][0] <= q:
                length = sorted_interv[interv_index][1] - sorted_interv[interv_index][0] + 1
                heapq.heappush(minHeap, (length, sorted_interv[interv_index][1]))
                interv_index += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            if minHeap:
                res[q] = minHeap[0][0]
            else:
                res[q] = -1

        return [res[q] for q in queries]