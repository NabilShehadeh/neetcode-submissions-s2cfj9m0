class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if Counter(t) == Counter(s):
            return True
        return False
        