class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initially we'll mention that we can obviously iterate through every pair of indices
        # we're essentially looking for target - nums somewhere in the array.
        # we can use a hashmap dictionary where we can store numbers we've already seen.
        # the plan is the following:
        # 1. we can create an empty hashmap to store our pairs.
        # 2. we iterate through the array with an index and value.
        # 3. we will calculate the difference until we find our target.
        # 4. if the diff exists in the hashmap then we return the index.
        # 5. if the diff does not exist in the hashmap then we end up storing the index 
        # 6. we essentially on pass through the array once. 
        # 7. hashmap helps us with constant time lookups. 

        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return