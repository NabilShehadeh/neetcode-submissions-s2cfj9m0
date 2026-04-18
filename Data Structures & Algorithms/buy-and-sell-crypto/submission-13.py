class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1 # since the buy pointer has to be ahead. 
        # intialize the max profit
        maxProfit = 0
        while r < len(prices): # within boundaries of the prices we're working with
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit
        