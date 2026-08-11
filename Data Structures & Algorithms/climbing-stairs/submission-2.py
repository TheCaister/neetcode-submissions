# at n, since you can take 2 steps, there are x ways to get to the n - 2 step, and y ways to get to the n - 1 step.
# you just need to add up x and y
# as long as we have the first 2 to start off from, we can start building it up
# quick solution, build up a list of size n, get the last element
# but tbh we should only need 3 vars?
# for 1, there's only 1 way. for 2, there are 2 ways, we can start from there
# on each step, x = y, and y becomes the new result

class Solution:
    def climbStairs(self, n: int) -> int:
        x = 1
        y = 2

        if n == 1:
            return 1

        for i in range(3, n + 1):
            x, y = y, x + y

        return y