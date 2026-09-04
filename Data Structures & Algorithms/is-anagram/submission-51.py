class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check the length of the anagrams, have to be equal
        # intiate the dictionaries
        # build a frequency map, where each character is a key and its count is the value.
        # increment the character 
        if len(s) != len(t):
            return False
        countT, countS = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # if value doesn't exist return 0
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT