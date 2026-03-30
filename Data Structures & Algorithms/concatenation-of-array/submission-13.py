class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        # we need to iterate twice and append the arrays
        for i in range(2):
            for n in nums:
                ans.append(n) # after completing the appending we return the answer.
        return ans
        