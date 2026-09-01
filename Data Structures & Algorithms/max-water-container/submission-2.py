class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # use two pointers at both ends to maximize the width

        res = 0
        l , r = 0, len(heights) - 1
        # calculate the current area (height = min of the two bars)
        while l < r:
            area = min (heights[l], heights[r]) * (r - l)
            res = max(res, area)
        
        # move the pointer pointing to the shorter bar, because limits.
            if heights[l] <= heights[r]:
                l += 1
            else: 
                r -= 1
        return res