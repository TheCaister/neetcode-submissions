# brute force, try out area for every possible index combo
# even that would be kinda inefficient, especially because you're bound by the smallest value in between, so you'll need to scan through and find that as well, so potentially n^3 time complexity there
# so maybe that's one of the challenges, how to efficiently find the smallest element within the range
# perhaps we can keep track of this smallest number as we go along
# 7 (smallest)
# then 1 becomes the smallest
# if it's just 7 and 1, we notice that we have gone down, so we either take 7 just by itself, or we take the index difference, and multiply it by the newest small number
# but at that point, there's no point considering 7 anymore, it will permanently be gimped by the 1, so we can effectly say that the "1" starts at index 7, then we move on
# a stack would work here, because we're buliding things up incremenetally, and need to pop the latest items
# so let's just start building up.
# 7,0 then 1,1. Notice that 1 is lower. process 7 (pop) then set 1 to the 7 index, repeat as necessary
# 7,2 add. 2,3, notice, pop and now 2,2. 2,4. could consolidate with the previous 2. 4.
# we'll end up with monotonic increasing stack
# but when should we start calculating and marking the areas?
# with this processing, we'll have the start times of all the values, but we can't blindly multiply them, seems that we'll have to do it on the fly
# if smaller, get the previous one up until the latest one
# at the end, since it's monotonic, we can actually process them one by one and continue checking out the largest area. we just need to make sure to include the intermediate ones as well
# should be n time and space, since each height is added and popped at most once, then the final scan at the end

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for idx, height in enumerate(heights):
            furthest_start = idx

            while stack and height < stack[-1][0]:
                prev_height, furthest_start = stack.pop()
                maxArea = max(maxArea, prev_height * (idx - furthest_start))
            
            stack.append((height, furthest_start))

        for height, start_idx in stack:
            maxArea = max(maxArea, (len(heights) - start_idx) * height)

        return maxArea
