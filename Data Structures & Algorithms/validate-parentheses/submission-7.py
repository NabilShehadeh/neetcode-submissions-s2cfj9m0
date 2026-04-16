class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(', ']': '[', '}': '{'}
        stack = [] # initiate an empty stack.
        # we're going to iterate through the input and run through a couple of conditionals
        # 1. is the stack empty.
        # 2. is the close parantheses/brace/bracket a match
        # 3. if it is a match we'll pop the stack if not then its false
        # 4. is the stack empty at the end if not its false since it has to be 
        for current in s:
            if current in "([{":
                stack.append(current) # essentially add in the opening p/b/brace
            else:# closing parantheses /bracket
                if not stack:
                    return False
                if stack[-1] != matching[current]:
                    return False
                stack.pop()
        return not stack

        