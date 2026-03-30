class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we'll initialize an index, and then utilize that to caluclate the differences
        # whatever matches our target will be the sum that we're looking for
        prevMap = {} # index init
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[n] = i
        return

        