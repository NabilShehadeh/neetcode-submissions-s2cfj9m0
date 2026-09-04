class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first we check the length of the anagrams, diff length not anagrams
        if len(s) != len(t):
            return False
        #initate the dictionaries
        countS, countT = {},{}
        # we want to iterate through each of the letters and add / return them
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        return countS == countT 