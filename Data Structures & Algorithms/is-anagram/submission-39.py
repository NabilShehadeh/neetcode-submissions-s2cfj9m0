class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # are they the same length?
        if len(s) != len(t):
            return False
        # intialize the dictionary
        countS, countT = {},{}
        # same length, then start iteration loop
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        return countS == countT
        # we want to simultenously compare them
        # return counts and t
        