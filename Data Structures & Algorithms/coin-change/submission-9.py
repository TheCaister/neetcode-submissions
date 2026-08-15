# if we think of it as decision tree, we gotta choose a coin at each stage
# only when it hits 0 exactly, we set it to the amount of coins it took us to get here
# so brute force would be x^y, x is len of coins, y is amount.
# perhaps, we can work backwards? because there should be cases where we
# run into the same amount of leftover money, and there should be a lowest path for
# that.
# one way to help with this is memoization
# we can also kinda do DP, going from amount = 0 to the max amount 10k which isn't too bad
# so for each amount, use all coins and see if there's a cached value
# if it hits 0, we set it to 1
# else for all other coins, get the smallest, and add 1 to it
# so it's amount * coins. and amount space. But since amount is bounded, we can be cheeky and say it's constant

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        best_changes = [float('inf')] * (amount + 1)

        if amount == 0:
            return 0
        
        for i in range(1, amount + 1):
            best_remaining_res = float('inf')
            print(f'i: {i}')
            for coin in coins:
                # print(f'coin: {coin}')
                remaining = i - coin

                if remaining == 0:
                    print(f'yes! we are at i={i} and coin {coin}')
                    best_changes[i] = 1
                    break
                
                if remaining < 0:
                    continue

                remaining_res = best_changes[remaining]

                if remaining_res < best_remaining_res:
                    best_remaining_res = remaining_res
                    best_changes[i] = best_remaining_res + 1

        return best_changes[-1] if best_changes[-1] != float('inf') else -1