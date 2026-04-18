class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first we'll do an initial length check
        if len(s) != len(t):
            return False
        # intialize the hashmaps
        countT, countS = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countT == countS