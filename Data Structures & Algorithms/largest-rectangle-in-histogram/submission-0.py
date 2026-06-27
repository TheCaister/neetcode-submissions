# brute force = exhaustive area calculation, n^2 time
# would it be possible to keep current running largest area?
# a tangent, how to find area between 2 indices? It would be range * lowest height
# let's say we have 2 pointers to possibly help us. what if we start at outer edge?
# it would seem that we only move inwards when it benefits us. so when there is height to be gained
# however, this wouldn't work in the case of a towering "island" in the middle. if we start outside, there's no easy way
# to figure out what's inside
# what if we put the 2 pointers starting in the middle?
# then, we would only move outwards if the height doesn't go down by more than 2.
# one thing to note is that the area is all bottlenecked by the lowest height.
# is there ever a case where not expanding because of height more than 2 hurts us? yes, if we have a veeery short but fat rectangle
# so it honestly seems 2 pointers wouldn't work
# 


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for index, height in enumerate(heights):
            # need to prepare an appropriate start
            start = index

            while stack and stack[-1][1] > height:
                last_start, last_height = stack.pop()
                start = last_start
                maxArea = max(maxArea, last_height * (index - last_start))

            stack.append([start, height])

        for start, height in stack:
            maxArea = max(maxArea, height * (len(heights) - start))

        return maxArea