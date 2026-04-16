class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # the targets are:
        # i need to check if i've seen a number before.
        # if i have seen the number then i would return true.
        # if i get through the whole array without finding duplicates then we return false.
        # I think the best way is to use a hashset approach.
        # 1. we'll create an empty hashset. 
        # 2. iterate through each number. 
        # 3. before adding the number we'll check if its already in my set. 
        # 4. if its in the set then we return true since we've found our duplicate. 
        # 5. if its not then we store it in the set and we'll continue. 
        # as for time complexity since we're building a record its O(1)
        # an alternative approach would be to compare every number with every other number. 
        # that's completely inefficient.
        # that's why I think its best if we use a set to track everything. 

        hashset = set()
        for n in nums: 
            if n in hashset:
                return True
            hashset.add(n)
        return False 
        