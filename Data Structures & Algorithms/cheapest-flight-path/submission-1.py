# i guess from src, do dfs for all paths, get the price, and update global minimum
# o (v + e)
# however, if we're past k but still haven't hit dst yet, that path is no bueno
# k = layovers, it's path excluding the extremities. if 1-2, it's 0 stops. but if over 2, it's n - 2

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                
                tmpPrices[d] = min(tmpPrices[d], prices[s] + p)

            prices = tmpPrices

        
        return -1 if prices[dst] == float("inf") else prices[dst]