class Solution:
    def scoreOfString(self, s: str) -> int:
        # first we'll initialize the resilt, then since we're looking for the adjacent result we'll add the ascii + 1 
        # for the iterations the loop will be a (s)-1 to avoid calculating the ending
        res = 0
        for i in range(len(s)-1):
            res += abs(ord(s[i])-ord(s[i+1]))
        return res
        