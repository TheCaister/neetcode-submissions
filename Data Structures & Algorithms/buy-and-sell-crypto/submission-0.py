# we want to maximise where end - start is the greatest
# brute force is exhaustive search, n^2 time. we just keep track of highest
# profit as we go, with default being 0
# could we be doing repeated work when going through all prices?
# when we move the start up, we take the diff and apply it to get the new profit
# we can't sort it, because the order matters here
# biggest edge case would be an island of 1, 1quadrillion side by side somewhere
# 

# 

# for each day, let's keep going until we hit a new low, then update the new low
# l = 0, r = 1
# if r < l, let's update l to r to give us a better chance guaranteed
# otherwise, keep moving right and update the profit
# do it until r reaches the end

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1
        
        return maxProfit

        