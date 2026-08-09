# there's a way to quickly check if the string is NOT valid, we'd have to make sure that right is not more than left + star, and vice versa
# normnally we can use stack to verify by processing through the inner most stack layers outwards. however, does the star throw a big wrench into things?
# if we do it this way, the main challenge is deciding what to do when we encounter a star...
# brute force - do a permutation of open closed brackets for all stars, and try them all out to see if any one of them is valid, n * 3^n time?

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = leftMax = 0


        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            
            if leftMax < 0:
                return False

            leftMin = max(leftMin, 0)

        return leftMin == 0