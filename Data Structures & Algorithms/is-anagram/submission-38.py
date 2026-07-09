class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if the lengths match, else false
        if len(s) != len(t):
            return False
        # intialize a dictionary for comparisons
        countS, countT = {},{}
        # simultenous iterations 
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        # return true if matching else false
        return countS == countT