class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', ']':'[', '}':'{'}
        stack = []

        for l in s:
            if l in mapping:
                if len(stack) == 0:
                    return False
                elif stack[-1] != mapping[l]:
                    return False
                stack.pop()
            else:
                stack.append(l)
        if len(stack) == 0:
            return True
        return False