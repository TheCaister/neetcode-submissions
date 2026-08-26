# let's think of it as a tree of decisions. at the very top, you can choose between all types
# when you pick one. in the next layer, you can either pick it again or pick coins after it
# along the way, we keep track of the total built up so far. if we hit exact match, that's one. if we are below, keep picking. if we are over, stop looking
# so there could be a lot of repeated work. let's say various combinations get you to the same coin index and left amount, let's cache it?
# so this cache would be amount * coins.len(), with time complexity being amount...?

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

        def dfs(i, a):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            if memo[i][a] != -1:
                return memo[i][a]

            res = 0
            if a >= coins[i]:
                res = dfs(i + 1, a)
                res += dfs(i, a - coins[i])

            memo[i][a] = res
            return res

        return dfs(0, amount)

        # cache = {}
        # found = 0

        # def dfs(amount_left, coin_index):
        #     if amount_left == 0:
        #         return 1
        #     if (amount_left, coin_index) in cache:
        #         return cache[(amount_left, coin_index)]
        #     if coin_index >= len(coins):
        #         return 0
            
        #     res = 0

        #     if coins[coin_index] <= amount_left:
        #         res = dfs(amount_left, coin_index + 1)
        #         res += dfs(amount_left - coins[coin_index], coin_index)
            
        #     return res
        
        # return dfs(amount, 0)