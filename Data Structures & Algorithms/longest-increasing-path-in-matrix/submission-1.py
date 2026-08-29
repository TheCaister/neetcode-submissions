# for each cell, do dfs until we can't increase anymore, cache the results to reduce repeated work, repeat this for every cell
# need to maintain current path as well to make sure we don't backtrack
# at each step, go into dfs
# at the very end, take the max + 1
# base case is out of bounds, in which case we'll return 0

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cur_largest = 0
        cache = {}
        cur_path = set()

        def dfs(x, y, prev):
            if (
                x < 0 or y < 0 or
                x >= ROWS or y >= COLS
            ):
                return 0
            if matrix[x][y] <= prev:
                return 0
            if (x, y) in cache:
                return cache[(x, y)]
            
            cur_path.add((x, y))
            max_path = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dx, dy in directions:
                # if (x + dx, y + dy) not in cur_path:
                max_path = max(max_path, dfs(x + dx, y + dy, matrix[x][y]))

            cur_path.remove((x, y))
            cache[(x, y)] = max_path + 1
            return max_path + 1

        for i in range(ROWS):
            for j in range(COLS):
                cur_largest = max(cur_largest, dfs(i, j, -1))
        
        return cur_largest