class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # comparison maxing
        sletters, tletters = {},{}
        for letter in s:
            sletters[letter] = sletters.get(letter, 0) + 1
        for letter in t:
            tletters[letter] = tletters.get(letter, 0) + 1
        if sletters == tletters:
            return True
        return False
        