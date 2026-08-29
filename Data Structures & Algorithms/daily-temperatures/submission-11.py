# brute force, n^2 solution, just check for every day
# on a particular day, we look only to the right until the end, keeping counter of
# days passed, if we reach the end, 0
# let's think about it.... as we go through the numbers
# for 30, as soon as we hit 38, we don't need to consider 30 anymore, we can remove it because we found the closest higher temperature
# but for 38, it's still in the running because we haven't found a higher temperature yet
# let's say we store all the elements that come after it. they all need to be equal or less than 38, or strictly neutral/decreasing. as soon as any higher temperature comes, then we'll start processing. stack would make sense here
# for the stack, it would make sense to store the value and the index, we populate the final index with the first idx (using diff), and at the end if there are any remaining, 
# this way, each element only enters/leaves once, so now it's n time and space complexity

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and stack[-1][1] < t:
                prev_i, _ = stack.pop()
                res[prev_i] = i - prev_i
            stack.append((i, t))

        return res

        
        