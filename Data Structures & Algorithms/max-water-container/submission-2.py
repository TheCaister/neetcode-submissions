# hmm let's say we have any abritrary 2 heights. how can we calculate the water? it'd be min(heights) * index diff (width)
# since when you visualise it, we're kinda dealing with ranges here, where we calculate the something in a range, 2 pointer/sliding window
# could be goated here
# brute force is exhaustive search through all combos, but sliding or pointer approach cna potentially bring it down to linear
# if we have any 2 random pointers. what happens when we move them?
# if you move left to the right, you're losing 1 width for sure, but you also might lose a crap ton of height. similar if you move right to the left
# on the opposite, if youy move the left o the left further, you'll get either a big boost in height, but you're getting 1 width for sure anywya
# is there a way to try isolate some f these variables, so that we know for sure whaty to do, and which direction to move the pointers towards?
# let's say they're all at the outer edges. if we move them in, it's 1 less width ALWAYS
# we would like to move the min of the pointers, because there's a chance you get a higher height
# if we start from the middle, and fan outwards instead...
# whether you move the left or right height,  ould mess you up fo rht efuture
# as you go in, if you move the lower one, you might win glory or lose, but you'll always lose if you move the bigger one
# if you're on the centre, anything could happen



class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_area = 0

        while l < r:
            max_area = max(max_area, min(heights[l], heights[r]) * (r - l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area