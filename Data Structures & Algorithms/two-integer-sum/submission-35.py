class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # array and an integer input, we need to return indicies that meet a specific target
        # our goal is how are we going to find that target score
        # we could reverse engineer this. 
        # first we would initialize a hashtable that we could iterate through and add for our numbers
        # if we have an array where the number is already included then we found our pair, if not we add it and continue.
        # we can find the differential by subtracting our target from the n

        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return 

        