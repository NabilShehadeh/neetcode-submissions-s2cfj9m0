class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # essentially if both the strings have the same amount of characters and the same frq of them by sorting we could
        # identifying if they are the same with the exact same characters. 
        # first we should check for their length's cause if its not the same then they aren't anagrams. 
        # order doesn't matter just the frequency. 
        # output is t/f 

        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        