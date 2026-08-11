# so you gotta hop out of the array to consider it done
# so we could exhaustively do all possible paths, starting from 0 and 1 index, picking whether to jump 1 or 2, stopping until we step out of bounds
# then getting the lowest price
# subtrees can be broken down into subproblems tho
# let's say we work backwards, for each index note down best price for that step
# so starting from the end, we can only use the price of the step itself, there's no other choice
#  from end - 1, we would also always use itself, because there's no point jumping to the end
# for every other guy after that, it's cur + min(step + 1, step + 2)
# at the end, we return the min of the last (or is it first?) two values

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        x, y = cost[-2], cost[-1]

        for i in range(len(cost) - 3, -1, -1):
            x, y = cost[i] + min(x, y), x

        return min(x, y)