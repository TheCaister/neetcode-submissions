# last digit, if 0, 0. If not 0, 1.
# second last digit. If 0, 0. If not 0, include itself and the number afterwards.
# additionally, check if it can be combined with the next letter, then add the number 2 afterwards
# 

class Solution:
    def numDecodings(self, s: str) -> int:
        x = y = z = 0

        def legitTwoDigit(dig1, dig2):
            if dig1 == "1":
                return True
            elif dig1 == "2" and (ord(dig2) - ord('0') <= 6):
                return True
            return False

        if s[-1] != "0":
            z = 1
        if len(s) == 1:
            return z
        
        if s[-2] != "0":
            y = z
            if legitTwoDigit(s[-2], s[-1]):
                y += 1
        if len(s) == 2:
            return y

        for i in range(len(s) - 3, -1, -1):
            x = 0
            if s[i] != "0":
                x = y
                if legitTwoDigit(s[i], s[i + 1]):
                    x += z
            
            # now we have the new x. Let's update y and z
            y, z = x, y

        return x