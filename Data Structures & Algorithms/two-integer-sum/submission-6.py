class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # first we're going to initlize the index
        prevMap = {} # -> index setup
        for i, n in enumerate(nums):
            #formula for calculating the diff
            diff = target - n
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[n] = i
        return
        