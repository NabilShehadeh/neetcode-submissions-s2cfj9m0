class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we're essentially looking at initalizing the hashset, then iterating through the nums
        # after iteration if its a duplicated return true, if not then we'll add it to the hashset
        # if all of the iterations are complete and no duplicates are found then we'll return false since nothing is found.
        hashset = set() # creation of a set
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False 
        