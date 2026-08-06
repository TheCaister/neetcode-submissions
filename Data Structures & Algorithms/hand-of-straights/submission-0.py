# first of all, len of hand must be a multiple of groupsize
# first thought is to sort, then try to build up the hands

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}

        for n in hand:
            count[n] = count.get(n, 0) + 1

        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            start = minHeap[0]

            for i in range(start, start + groupSize):
                if i not in count:
                    return False
                
                count[i] -= 1

                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    
                    heapq.heappop(minHeap)

        return True
        