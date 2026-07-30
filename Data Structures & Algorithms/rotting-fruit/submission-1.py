# bfs
# if no fruits have become rotten at one of the layers, return -1 because we'll never make them bad
# add all rotten fruits first. 
# then, rot the adjacent fruits before adding them, let's keep track of fruits that have been corrupted

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))

        while queue:

            res += 1

            for i in range(len(queue)):
                cur_r, cur_c = queue.popleft()

                directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

                for dx, dy in directions:
                    new_r, new_c = cur_r + dx, cur_c + dy

                    if(
                        (new_r >= 0 and new_c >= 0) and
                        (new_r < ROWS and new_c < COLS) and
                        grid[new_r][new_c] == 1
                    ):
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        if res > 0:
            return res - 1
        else:
            return 0