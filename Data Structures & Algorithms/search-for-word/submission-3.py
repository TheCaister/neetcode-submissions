# wriggle around, building up the words until we find a match
#  (m * n) * 4^(length of word)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        visited = set()

        def dfs(x, y, cur_str):
            if ((x, y) in visited
                or x >= ROWS or y >= COLS
                or x < 0 or y < 0
                or len(cur_str) > len(word)
            ):
                return False
            
            cur_str += board[x][y]
            # print(cur_str)

            if cur_str == word:
                # print("Found!")
                return True

            visited.add((x, y))

            if (
                dfs(x + 1, y, cur_str) or
                dfs(x, y + 1, cur_str) or
                dfs(x - 1, y, cur_str) or
                dfs(x, y - 1, cur_str)
            ):
                return True
            
            visited.remove((x, y))

        for row in range(ROWS):
            for col in range(COLS):
                visited = set()
                if dfs(row, col, ""):
                    return True

        return False