class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Over head logic, 1. initialize the hashset with set(), then iterate to find any duplicates, if any duplicates are found
        # we'll return true then include an addition to the n and if no duplicates are found at the end of it we'll return false
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        