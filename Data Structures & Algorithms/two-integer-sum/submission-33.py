class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # mapping the value to the index of that 
        #iterate through every value
        for i, n in enumerate(nums):
            #check the diff
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i # if we don't find our solution we update the hashmap.
        return 