class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # first we'll initialize the array that we're going to append
        # for loops with i then n
        ans =[]
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans