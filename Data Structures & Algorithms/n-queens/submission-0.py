# for each line, there are n choices. so n^n? Well actually as you move down, you'll get less and less options, so n! factorial
# I think a main challenge would be how to check if queen is diagonal. i think you can just subtract the 2 positions, and make sure it's not the same
# 


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []

        cur_line_indexes = []

        def dfs(line_num):
            if line_num >= n:
                cur_res = []

                # n = 3, "..". Let's say line can be 0, 1, 2

                for line in cur_line_indexes:
                    cur_str = "." * (n - 1)
                    cur_str = cur_str[:line] + "Q" + cur_str[line:]
                    cur_res.append(cur_str)
                
                res.append(cur_res)

                return

            for i in range(n):
                goAhead = True
                for existing_line_index in range(len(cur_line_indexes)):
                    if cur_line_indexes[existing_line_index] == i:
                        goAhead = False
                        break
                    if line_num - existing_line_index == abs(i - cur_line_indexes[existing_line_index]):
                        goAhead = False
                        break

                if goAhead:
                    cur_line_indexes.append(i)
                    dfs(line_num + 1)
                    cur_line_indexes.pop()

        dfs(0)

        return res