# how do you make sure parentheses are well formed? usually stack should do the trick
# strings are all of size n * 2 one for opening and closing brackets
# at each point, we can ask if we should put an open or closed bracket
# for open, we can place it down if it's less/equal to half of remaining guys
# for closed, we can only proceed if there's an open bracket last in the stack. otherwise, we skip


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def dfs(opened, closed, cur_str):
            if closed == n and opened == n:
                res.append(cur_str)
                return
            
            if opened < n:
                cur_str += "("
                dfs(opened + 1, closed, cur_str)
                cur_str = cur_str[:-1]

            if closed < opened:
                cur_str += ")"
                dfs(opened, closed + 1, cur_str)
                cur_str = cur_str[:-1]

        dfs(0, 0, "")

        return res