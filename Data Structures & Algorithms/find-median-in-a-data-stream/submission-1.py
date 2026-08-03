# naive/one way, maintain a sorted list, which we can use binary search to find the position, but
# we'll need to shift things up, so o(n), but blazing fast on the retrieve path
# or, o(n) time and space on retrieve path if we store things in a heap, we pull x amount of times
# well, there is no functionality to delete elements, i wonder if we can use that to our advantage
# maybe we can continuously update median as we add new numbers


# maintain 2 heaps, 
# everytime we add, if it's bigger than heappop of bigHeap, put in bigHeap, and vice versa
# for odd case, find the bigger heap and get the end elements

class MedianFinder:

    def __init__(self):
        self.smallerHeap = []
        self.biggerHeap = []
        
        heapq.heapify(self.smallerHeap)
        heapq.heapify(self.biggerHeap)

    def addNum(self, num: int) -> None:
        if self.biggerHeap and num >= self.biggerHeap[0]:
            heapq.heappush(self.biggerHeap, num)
        else:
            heapq.heappush(self.smallerHeap, -num)

        while abs(len(self.smallerHeap) - len(self.biggerHeap)) > 1:
            if len(self.smallerHeap) > len(self.biggerHeap):
                toBeMoved = -heapq.heappop(self.smallerHeap)
                heapq.heappush(self.biggerHeap, toBeMoved)
            else:
                toBeMoved = -heapq.heappop(self.biggerHeap)
                heapq.heappush(self.smallerHeap, toBeMoved)

    def findMedian(self) -> float:
        if len(self.smallerHeap) > len(self.biggerHeap):
            return -self.smallerHeap[0]
        elif len(self.biggerHeap) > len(self.smallerHeap):
            return self.biggerHeap[0]
        else:
            return (-self.smallerHeap[0] + self.biggerHeap[0]) / 2        