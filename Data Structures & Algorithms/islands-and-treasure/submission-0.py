# for each land cell, do traversal either dfs/bfs.
# n^2 * 4^(n^2)
# or, perhaps we can stop early when we reach a before-reached land, adding its value to the current length
# build up distance as we go. when we reach treasure, see if we can update min distance. otherwise when we reach visited land, add that to the cur length and return
# initialise a default value so that the land stays the same if nothing is found
# that way, we traverse each land cell once, bringing down the tiim ecomplexity

# scan through the grid and find all grids w/ the treeasure
# prep a queue w/ the treasure
# each step, flush the entire queue. 
# for each cell processing, set each adjacent inf block to itself + 1, then add the adjacent blocks to the queue
# 

from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        
        while queue:
            for i in range(len(queue)):
                cur_r, cur_c = queue.popleft()

                directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

                for dy, dx in directions:
                    new_r, new_c = cur_r + dy, cur_c + dx

                    if (
                        (new_r >= 0 and new_c >= 0) and
                        (new_r < ROWS and new_c < COLS) and
                        (new_r, new_c) not in visited and
                        grid[new_r][new_c] == 2147483647
                    ):
                        grid[new_r][new_c] = grid[cur_r][cur_c] + 1
                        queue.append((new_r, new_c))
                        print((new_r, new_c), grid[cur_r][cur_c])