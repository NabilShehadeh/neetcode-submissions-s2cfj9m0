class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we'll essentially work on finding the difference and for the two numbers that we get that difference aligned
        # those we'll be our targets, furthermore, we'll ensure that everything is appended and compared
        prevMap = {} # initalizing the index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[n] = i
        return
        