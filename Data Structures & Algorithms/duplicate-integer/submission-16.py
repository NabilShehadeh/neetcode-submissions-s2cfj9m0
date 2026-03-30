class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # higher up logic: going to create a set, if we find a duplicate we return it true then add if we don't have duplicates we'll
        # return it false
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        