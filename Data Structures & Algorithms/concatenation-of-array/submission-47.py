class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2): # how many times we're iterating
            for n in nums:
                ans.append(n)
        return ans
