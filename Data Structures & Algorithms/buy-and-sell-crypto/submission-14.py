class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # intialize the pointers
        l,r = 0,1
        # left is buying and right is selling
        maxP = 0 # profit initialization
        while r < len(prices) : 
            # check if profitable transaction
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit) # whatever the max while be assigned.
            else:
                l = r # if we found the lowest price we could find
            r += 1
        return maxP