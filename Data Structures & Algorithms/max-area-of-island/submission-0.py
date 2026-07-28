# this could be done very similarly to the num of islands problem

from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        max_area = 0

        def bfs(r, c):
            cur_area = 0
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                cur_r, cur_c = queue.popleft()
                cur_area += 1

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dx, dy in directions:
                    new_r, new_c = cur_r + dx, cur_c + dy


                    if (
                        new_r in range(ROWS) and
                        new_c in range(COLS) and
                        grid[new_r][new_c] == 1 and
                        (new_r, new_c) not in visited
                    ):
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
            
            return cur_area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(bfs(r, c), max_area)

        return max_area