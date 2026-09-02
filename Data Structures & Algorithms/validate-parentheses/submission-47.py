class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        otoclose = {']':'[', ')':'(', '}':'{'}
        for char in s:
            if char in otoclose:
                if stack and stack[-1] == otoclose[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack