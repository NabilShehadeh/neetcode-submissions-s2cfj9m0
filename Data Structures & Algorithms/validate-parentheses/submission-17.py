class Solution:
    def isValid(self, s: str) -> bool:
        seen = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []
        for current in s:
            if current in "[{(":
                stack.append(current)
            else:
                if not stack:
                    return False
                if stack[-1] != seen[current]:
                    return False
                stack.pop()
        return not stack
        