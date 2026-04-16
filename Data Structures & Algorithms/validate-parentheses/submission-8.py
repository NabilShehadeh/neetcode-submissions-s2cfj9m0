class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(', ']': '[', '}': '{'}
        stack = []
        # Logic behind the code:
        # 1. is the parentheses open or closed?
        # 2. if its open add it to the stack.
        # 3. if its a closed parantheses we'll move on to more conditionals.
        # 4. is the stack empty first, with no matching opening.
        # 5. does the top parantheses match the current closing bracket. 
        # 6. if so, then we'll remove that from the stack. 
        # 7. by the end of the iteration we should see that we have an empty stack.
        # 8. if our stack is essentially still containing some elements then its false.
        # 9. since we have to have an empty stack by the end of everything. 
        for current in s:
            # for the opening paren.
            if current in "{[(":
                stack.append(current)
            else:
                if not stack:
                    return False
                if stack[-1] != matching[current]:
                    return False
                stack.pop()
        return not stack