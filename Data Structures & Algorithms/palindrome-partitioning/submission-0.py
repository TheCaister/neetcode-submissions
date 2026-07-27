class Solution:
    def isPalin(self, s, i, j):

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True


    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur_part = []

        def dfs(i):
            if i >= len(s):
                res.append(cur_part.copy())

            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    cur_part.append(s[i:j + 1])

                    dfs(j + 1)

                    cur_part.pop()

        dfs(0)

        return res
        