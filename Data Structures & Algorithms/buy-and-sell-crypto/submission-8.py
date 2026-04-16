class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # here we intialize our pointers 
        l, r = 0,1 #because our selling is always going to be ahead of our buying. 
        maxP = 0 
        while r < len(prices): # here we ensure we're within bounds. 
            # calculate the profit and see if we have to update it.
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit) # return the max profit and the day it took place. 
            else:
                l = r # this ensures we're buying at the lowest date. 
            r += 1 # either way we want to iterate till the end.
        return maxP 

        