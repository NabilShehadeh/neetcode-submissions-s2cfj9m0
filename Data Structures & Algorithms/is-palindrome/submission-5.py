class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first we're going to initialize the pointers, since we're going with a two pointer solution
        l , r = 0, len(s) - 1 # to start the pointer on the opposite end
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l , r = l + 1, r - 1
        return True



    def alphaNum(self, c): # this ensures we can check if the entity we're looking at is alphanumeric else we skip it

        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        