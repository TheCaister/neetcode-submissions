# build up map of numbers to available digits?
# 3^n time. n extra memory

class Solution:

    num_to_dig = {
        "2": ("a", "b", "c"),
        "3": ("d", "e", "f"),
        "4": ("g", "h", "i"),
        "5": ("j", "k", "l"),
        "6": ("m", "n", "o"),
        "7": ("p", "q", "r", "s"),
        "8": ("t", "u", "v"),
        "9": ("w", "x", "y", "z"),
    }

    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        self.cur_str = ""

        if len(digits) == 0:
            return res

        def dfs(i):
            if i >= len(digits):
                res.append(self.cur_str)
                return
            
            avail_digits = self.num_to_dig[digits[i]]

            for digit in avail_digits:
                self.cur_str += digit
                dfs(i + 1)
                self.cur_str = self.cur_str[:-1]

        dfs(0)

        return res
