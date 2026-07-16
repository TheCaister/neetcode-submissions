# there's a range of values of banana eating speed available for Koko
# slowest speed of 1 banane per hour means sum(piles) hours. this is the max amount of hours
# fastest speed is max of piles, in which case it's len(piles) amount of hours
# n log n solution

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        lowest = float('inf')

        def can_consume_all_piles(speed):
            hours_consumed = 0
            pile_index = 0

            for i in range(len(piles)):
                hours_consumed += math.ceil(piles[i] / speed)

            if hours_consumed > h:
                return False
            else:
                return True
            
        print(f'slowest: {l}, fastest: {r}')

        while l <= r:
            mid_speed = l + ((r - l) // 2)

            if can_consume_all_piles(mid_speed):
                lowest = min(lowest, mid_speed)
                r = mid_speed - 1
            else:
                l = mid_speed + 1

        return lowest