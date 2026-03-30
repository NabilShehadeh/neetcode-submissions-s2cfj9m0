class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #higher up idea, we want to return ans, by addaing nums to it
        # we need to iterate with a range of 2, where everything s added
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
        