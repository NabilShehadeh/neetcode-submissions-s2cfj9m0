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
        # the essential goal here is to find if we have duplicates but since we can't have duplicates we'll maximize the hashset
        # after that we keep iterating until we don't have duplicates or everything is resolved
        