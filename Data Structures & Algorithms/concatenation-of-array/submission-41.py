class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # since we need to concatenate and then iterate twice we should utilize the range
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
        