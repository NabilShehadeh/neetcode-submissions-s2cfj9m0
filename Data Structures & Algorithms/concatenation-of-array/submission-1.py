class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] # here we are initializing the array
        for i in range(2):
            # iterating through it twice
            for n in nums:
                ans.append(n)
        return ans
        