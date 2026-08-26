# let's think of it as a tree of decisions. at the very top, you can choose between all types
# when you pick one. in the next layer, you can either pick it again or pick coins after it
# along the way, we keep track of the total built up so far. if we hit exact match, that's one. if we are below, keep picking. if we are over, stop looking
# so there could be a lot of repeated work. let's say various combinations get you to the same coin index and left amount, let's cache it?
# so this cache would be amount * coins.len(), with time complexity being amount...?

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        coins.sort()

        def dfs(amount_left, coin_index):
            if amount_left == 0:
                return 1
            if coin_index >= len(coins):
                return 0
            if (amount_left, coin_index) in cache:
                return cache[(amount_left, coin_index)]
            
            res = 0

            if coins[coin_index] <= amount_left:
                res = dfs(amount_left, coin_index + 1)
                res += dfs(amount_left - coins[coin_index], coin_index)
            
            cache[(amount_left, coin_index)] = res
            return res
        
        return dfs(amount, 0)