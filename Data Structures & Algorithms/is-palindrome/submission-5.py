# case insensitive, should consider converting all to 1 case as we go
# we can reverse and check
# we can put pointers at either end, and either go in or out.
# let's try out, this will depend a bit on even vs odd num of chars
# while l < r, keep going.

# ignores non alphanumeric
# can keep moving until we reach one

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            left_char_upper = s[l].upper()
            right_char_upper = s[r].upper()

            while l < r and not (ord(left_char_upper) >= ord('A') and ord(left_char_upper) <= ord('Z')) and not (ord(left_char_upper) >= ord('0') and ord(left_char_upper) <= ord('9')):
                # print(f'Left: {left_char_upper}, Right: {right_char_upper}')
                l += 1
                left_char_upper = s[l].upper()
            
            while l < r and not (ord(right_char_upper) >= ord('A') and ord(right_char_upper) <= ord('Z')) and not (ord(right_char_upper) >= ord('0') and ord(right_char_upper) <= ord('9')):
                r -= 1
                right_char_upper = s[r].upper()

            # print(f'Left: {left_char_upper}, Right: {right_char_upper}')

            if l < r and s[l].upper() != s[r].upper():
                return False

            l += 1
            r -= 1

        return True