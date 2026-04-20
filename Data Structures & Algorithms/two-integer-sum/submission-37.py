class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums array, given our target. 
        # return i and j

        # formula to calculate the difference. 
        # intiate a dictionary, {}
        
        # iterate through the list 
        # utilize enumerate to give us the indicies and tie them to the numbers
       
        # compute the diff
        # if we have the diff we've found our pair.
        # if not we continue iterating until we do.

        prevMap = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in prevMap:
                return[prevMap[diff], index]
            prevMap[number] = index
        return prevMap
        