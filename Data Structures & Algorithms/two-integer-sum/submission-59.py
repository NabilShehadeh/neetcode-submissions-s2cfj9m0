class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # intialize the hashmap
        prevMap = {}
        #iterate through the array
        for i, n in enumerate(nums):
            # calculate the diff
            diff = target - n
            # check if complement exists
            if diff in prevMap:
                #return the value
                return [prevMap[diff], i]
            #store current number if it isn't 
            prevMap[n] = i # key is n value is i
        return 