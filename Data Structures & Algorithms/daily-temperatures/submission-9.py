# so on the hottest day and after, result would be all 0
# one way would just to do exhaustive search, so n^2 time complexity
# for each, you keep going up, keeping track of days until you either hit the end (put 0)
# or, if you hit a hotter day, set the result at that.
# but, there could definitely be some repeated work here.
# if you process index a until c, when you get to index a+1, do you need to 
# process the overlaps again? or can we do some tricks here?
# do we always need to scan ahead to figure out the answer for an index?
# what if we go the other way? from the end, work backwards
# so let's pretend we're working backwards
# if a-1 is smaller than a, then set it to 1.
# if a-2 is smaller than a, there's a chance it's also smaller than a-1
# this is why I don't think working from the end is the greatest approach. you
# need to keep track of a strictly increasing list of numbers, and do various
# calculations, so time complexity stays the same, and it's more complex,
# and we're trying to optimise for shortest amount of time afterwards, working
# backwards doesn't make sense because there's a lot of stuff to juggle
# what if we go back to working forwards then
# that strictly increasing list might give us a hint...
# what if we store the index and value in a list...
# [30, 0], [38, 1]
# we could update it to be cur-peek indexes, then get rid of the 30, because we're done processing it
# [38, 1], [30, 2] - [0:1]
# Let's do nothing for now, we can't process anything yet
# [38, 1], [30, 2], [36, 3]
# so, we peek and find it's smaller, let's process
# [38, 1], [36, 3] - [0:1, 2:1]
# [38, 1], [36, 3], [35, 4]
# [38, 1], [36, 3], [35, 4], [40, 5] - Process
# what we're essentially doing is strictly decreasing stack, and keep popping
# when a bigger value comes in. 
# since each element only gets added/popped at most once, it's o(n) time and space
# the stack works because it allows us to process all the PREVIOUS elements when a trigger
# element comes in.

# set up result array of 0s
# 1. push
# 2. while peek.val is LESS, process
# 3. while processing, pop, result[pop.index] = cur.index - pop.index

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, v in enumerate(temperatures):
            # print(stack)

            while stack and stack[-1][1] < v:
                popped_i, popped_v = stack.pop()

                result[popped_i] = i - popped_i
            
            stack.append([i, v])
        
        return result

        