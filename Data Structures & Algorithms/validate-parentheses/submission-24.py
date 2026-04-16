class Solution:
    def isValid(self, s: str) -> bool:
        # essentially we'll utilize a stack, since we're moving in sequence and everything has to match. 
        # after intializing the stack and a dictionary we can use for comparisions etc...
        # if our stack has no values at all then we can exit right away. 
        # if our stack has values we take a look at what we have. 
        # if we have an open parantheses we add it to the stack and continue. 
        # if we have a closed parantheses we look at what we have at the top, if it matches then we pop it and remove it. 
        # the goal is that by the end of the stack iterations we should have an empty stack. 
        # everything else results in a false scenario. 

        complete = {']':'[', ')':'(', '}':'{'}
        stack = []
        for current in s: # this takes a look at the current input and decides whether to add, proceed or fail. 
            if current in "[{(":
                stack.append(current)
            else:
                if not stack:
                    return False
                if stack[-1] != complete[current]:
                    return False
                stack.pop()
        return not stack 
        