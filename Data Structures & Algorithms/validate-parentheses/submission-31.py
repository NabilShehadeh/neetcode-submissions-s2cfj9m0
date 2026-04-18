class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        complete = {']':'[', ')':'(', '}':'{'}
        for current in s:
            if current in "{[(":
                stack.append(current)
            else:
                if not stack: #is the stack empty, return it false since its invalid.
                    return False # if the stack is n
                if stack[-1] != complete[current]: # the immediate top level of the stack and our input are mismatched
                    return False
                stack.pop()
        return not stack