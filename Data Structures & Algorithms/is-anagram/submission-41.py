class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # utilize a hashmap to track the frequencies.
        # if match then anagrams

        # 1. if two strings are diff lengths return false
        # 2. create two hash maps to store character frequencies for each string.
        # 3. iterate through both strings at the same time: increase count for both maps
        # 4. compare maps and return.

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT