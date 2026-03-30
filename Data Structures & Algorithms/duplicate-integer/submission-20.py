class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # since we can't have duplicates we can utilize hashsets as sets
        # intialize the hashset
        # then we can run the comparisons to figure out if any value appears more than once.
        # if its in the array we say true and if we iterate through it all and find nothing
        # then its false.
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        