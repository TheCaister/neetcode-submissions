class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}


        def dfs(i, isBuying):
            if i >= len(prices):
                return 0
            if (i, isBuying) in dp:
                return dp[(i, isBuying)]

            # preserve state, and keep going
            coolDownPath = dfs(i + 1, isBuying)

            if isBuying:
                curProfit = dfs(i + 1, False) - prices[i]
                dp[(i, isBuying)] = max(curProfit, coolDownPath)
            else:
                curProfit = dfs(i + 2, True) + prices[i]
                dp[(i, isBuying)] = max(curProfit, coolDownPath)

            return dp[(i, isBuying)]
        
        return dfs(0, True)