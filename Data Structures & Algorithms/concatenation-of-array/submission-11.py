class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # we're looking to add together arrays
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
        