class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = '' # first we'll intialize empty strings for filtered characters
        for c in s: # here we'll iterate through each character. 
            if c.isalnum(): # then we'll check if its alphanumeric
                newStr += c.lower() # we'll convert it to lowercase and append.
        return newStr == newStr[::-1] # then we'll compare with the reverse.
        # either get a true or false situation


        