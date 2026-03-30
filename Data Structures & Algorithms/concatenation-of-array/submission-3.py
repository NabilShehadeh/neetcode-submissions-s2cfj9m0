class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # initialize the empty array that we're going to append
        ans = []
        # going to iterate through it twice
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
        