class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we need to combine both arrays into one
        prevMap = {} # here we initialize the index.
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return       