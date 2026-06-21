# classically can solve w/ stack, as it helps you cancel out the latest open bracket, and opens up the previous one
# open brackets, keep adding. closing bracket? see if the popped value matches. if not, False
# edge cases would be when the stack is empty. if stack empty, we also False, as it's invalid and suggests extra closing


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_mapping = {
            '{': '}',
            '(': ')',
            '[': ']',
            '}': '{',
            ')': '(',
            ']': '[',
        }

        stack = []

        for c in s:
            if c in ['{', '(', '[']:
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                latest = stack.pop()
                if latest != bracket_mapping[c]:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False