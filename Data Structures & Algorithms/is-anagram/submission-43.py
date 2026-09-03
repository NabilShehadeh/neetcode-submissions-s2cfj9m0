class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # have to be the same length to be an anagram
        countS, countT = {},{}

        for i in range(len(s)):
            # takes the char at position, adds 1 to that count and stores it back in dict.
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

