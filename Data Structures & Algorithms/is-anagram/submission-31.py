class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # inputs s & t
        # sort s and sort t to compare equal

        # if exact characters return true.
        # if not exact return false.

        if sorted(s) != sorted(t):
            return False
        return True
        