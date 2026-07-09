# brute force n^2 exhaustive search for profit
# we're maximising prices[idx2] - prices[idx1]
# ok, let's imagine the stock price, and see if we can see something
# order matters, you can't sell in the past, buy in the future etc. sell must be after buy
# buy low, sell high
# i start w/ current price, and start seeing the selling prices, updating max as i go
# if I see new floor, update to new floor, and repeat the process

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        startDate = 0

        while startDate < len(prices):
            startPrice = prices[startDate]
            endDate = startDate + 1
            while endDate < len(prices) and prices[endDate] > prices[startDate]:
                maxProfit = max(maxProfit, prices[endDate] - prices[startDate])
                endDate += 1
            
            startDate = endDate

        return maxProfit