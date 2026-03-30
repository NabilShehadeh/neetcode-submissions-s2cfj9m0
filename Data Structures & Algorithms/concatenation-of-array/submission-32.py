class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # we initially want to return the array doubled, so we'll need 2 runs
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
        