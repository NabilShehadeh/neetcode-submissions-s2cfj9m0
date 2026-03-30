class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #first we'll create an empty array
        ans = []
        for i in range(2):
            #n in nums
            for n in nums:
                ans.append(n)
        return ans