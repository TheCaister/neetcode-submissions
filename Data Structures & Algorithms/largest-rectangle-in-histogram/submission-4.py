# brute force, check each permutation, n^3 time to scan the ranges and check if 
# there are any lower bars in the middle somewhere
# no matter what, each height needs to be checked


# if we force it into strictly increasing list, then we just need
# to get the starting index of a particular height
# then at the end, we calculate the heights
# we could build up a stack
# if cur <= prev, then we consolidate by popping, using the prev index, and using the cur value
# otherwise add
# at the end, we go through the stack


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            new_i = i

            while stack and h < stack[-1][1]:
                prev_i, prev_h = stack.pop()

                cur_area = (i - prev_i) * prev_h

                maxArea = max(maxArea, cur_area)

                new_i = prev_i
            
            stack.append([new_i, h]) 

        for start_i, h in stack:
            cur_area = (len(heights) - start_i) * h
            maxArea = max(maxArea, cur_area)

        return maxArea
        