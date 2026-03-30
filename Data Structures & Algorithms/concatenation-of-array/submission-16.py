class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        # creation of an array then appending twice as stated
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
        