class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # intialize the ans
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
