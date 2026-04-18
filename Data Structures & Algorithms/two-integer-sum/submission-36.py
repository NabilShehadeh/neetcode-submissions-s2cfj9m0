class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using a hash table to iterate through the indicies and the values to compare. 
        # then we'll calculate a difference to find out our target and compare.
        # if we have two numbers that have the same diff then they essentially are our targets.
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i # we'll ensure that the values are stored properly
        return
        