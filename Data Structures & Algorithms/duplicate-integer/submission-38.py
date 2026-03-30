class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset situation and can't have duplicates, after going through ensure we append
        hashset = set()
        for n in nums: 
            if n in hashset:
                return True
            hashset.add(n)
        return False
        