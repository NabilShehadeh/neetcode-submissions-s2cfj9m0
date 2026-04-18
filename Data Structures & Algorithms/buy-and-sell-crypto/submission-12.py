class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 
        l , r = 0 , 1 
        while r < len(prices): # ensure that the r is within boundaries 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l] # profit calculation to compare and contrast as we iterate
                maxP = max(maxP, profit)
            else:
                # if the r pointer is lower than the l pointer then we'll shift the left to get a better buying opportunity
                l = r 
            r += 1 # to keep iterating if everything else looks good
        return maxP

        