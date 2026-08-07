class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # intialize pointers
        l,r = 0,1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r # skip to the right if r is lower than l 
            r += 1
        return maxP