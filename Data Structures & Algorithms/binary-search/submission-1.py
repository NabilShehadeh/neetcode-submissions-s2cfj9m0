class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search
        # L, R = 0, len(nums) - 1
        # Midpoint = R - L // 2, index calculation, could be many times

        # while loop, exit when done iterating
        # compare on values, convert index = value

        # if target not found, return -1
        # if we find target, return index of target

        # if target > Midpoint: L = M
        # if target < Midpoint: R = M

        # if target = Midpoint, return index value

        

        L = 0
        R = len(nums) - 1

        while L <= R:
            Midpoint = R - L // 2
            if target == nums[Midpoint]:
                return Midpoint
            elif target > nums[Midpoint]:
                L = Midpoint + 1
            elif target < nums[Midpoint]:
                R = Midpoint - 1
        return -1


        
            

        