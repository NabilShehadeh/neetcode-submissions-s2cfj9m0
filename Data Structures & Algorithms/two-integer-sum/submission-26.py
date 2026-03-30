class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # essentially we're looking at using hashing, then creating an index table and referencing that to see what two 
        # numbers end up meeting our target
        prevMap = {} # creation of the index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return 

        