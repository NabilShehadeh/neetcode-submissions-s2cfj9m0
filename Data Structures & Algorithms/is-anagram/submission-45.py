class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # they can't be diff lenghts
        # we're going to take the ones at index, count them and add up for both strings to compare.
        countS, countT = {},{}
        for i in range(len(s)):
             countS[s[i]] = 1 + countS.get(s[i], 0)
             countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT