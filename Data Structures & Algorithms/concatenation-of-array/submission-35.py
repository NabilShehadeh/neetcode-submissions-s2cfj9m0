class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # we need to create an array and then iterate and combine it twice
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
        