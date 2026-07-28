# could do topological traversal, go to every cell, and spread out.
# make sure to keep track of visited cells. only for unvisited island cells, begin spreading, and add 1 at the end
# n^2 time and space

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        islands = 0

        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                cur_r, cur_c = queue.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dx, dy in directions:
                    new_r, new_c = cur_r + dx, cur_c + dy

                    if (
                        new_r in range(ROWS) and
                        new_c in range(COLS) and
                        grid[new_r][new_c] == "1" and
                        (new_r, new_c) not in visited
                    ):
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
        