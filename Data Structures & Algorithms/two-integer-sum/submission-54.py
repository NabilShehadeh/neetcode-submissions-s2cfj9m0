class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # every previous element is here val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[n] = i # if there is no solution we add it to the hashmap.
        return             