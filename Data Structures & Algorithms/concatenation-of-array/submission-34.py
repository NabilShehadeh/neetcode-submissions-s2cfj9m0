class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # here we initalize an empty result list
        # use a loop that runs twice
        # inside the loop we'll iterate through every element
        # append num to the result list or assign it
        # return the resulting array ans.
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
        