# holy crap i can think of it like bfs

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0

            for i in range(l, r + 1):
                cur_distance = i + nums[i]
                farthest = max(farthest, cur_distance)
            
            l = r + 1
            r = farthest

            res += 1


        return res